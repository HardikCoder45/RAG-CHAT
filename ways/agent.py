from langchain.tools.retriever import create_retriever_tool
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain_core.tools import Tool
from langchain.agents import create_openai_tools_agent
from langchain import hub
from langchain.agents import AgentExecutor

class AgentExecutorWrapper:
    def __init__( ):
        # Initialize any necessary attributes if needed
        pass

    def create_agent(  model, db, google_api, google_cse_id):
     try:
        # Initialize Google Search API Wrapper
        search = GoogleSearchAPIWrapper(google_api_key=google_api, google_cse_id=google_cse_id, k=3)

        # Define Google Search Tool
        google_tool = Tool(
            name="google_search",
            description="Search Google for recent results.",
            func=search.run
        )
        
        # Define Document Retrieval Tool
        vector_db = db.as_retriever()
        docs_tool = create_retriever_tool(vector_db, "Docs_Tool", """Context:
You are an advanced retriever tool with access to a wide array of documents. Your task is to search through these documents and provide the most relevant information based on the query provided. Your response should be clear, concise, and comprehensive, highlighting the key points and details from the documents.

Instructions:

Search Thoroughly: Scan all available documents to find the most relevant information related to the query.
Summarize Clearly: Present the information in a well-organized manner, summarizing the key points effectively.
Highlight Key Details: Emphasize important facts, data, and insights from the documents.
Provide Context: Where necessary, provide additional context to ensure the information is fully understood.
Format Professionally: Use bullet points, headings, and paragraphs to structure the response for easy readability.""")
        
        tools = [docs_tool, google_tool]
        
        # Pull the prompt from the hub
        prompt = hub.pull("hwchase17/openai-functions-agent")
        
        # Create the OpenAI Tools Agent
        agent = create_openai_tools_agent(model, tools, prompt)
        
        # Initialize AgentExecutor
        agent_executor = AgentExecutor(tools=tools, agent=agent, verbose=True)
        status = "OK"
        return [status,agent_executor]
     except Exception as e:
        agent_executor = e
        status = "error"
        return [status, agent_executor]
