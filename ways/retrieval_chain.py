from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain


class retrival_chain:
    def __init__():
        pass
    def create_chain(model,db):
        try:
         prompt = ChatPromptTemplate.from_template(""" You are an advanced retrieval chain designed to search through a comprehensive set of documents to extract the most relevant information based on the provided query. Your task is to deliver a precise, informative, and well-organized response that highlights the essential details and provides context where necessary.

Instructions:

Thorough Search: Conduct an exhaustive search through all available documents to find the most pertinent information related to the query.
Clear Summarization: Summarize the retrieved information in a coherent and concise manner, emphasizing the key points.
Highlight Key Details: Focus on important facts, data, and insights from the documents.
Contextual Explanation: Offer additional context to ensure the retrieved information is fully comprehensible.
Professional Formatting: Organize the response using bullet points, headings, and paragraphs to enhance readability. context:- {context}, question: {input}""")
         chain = create_stuff_documents_chain(model,prompt)
         retriever = db.as_retriever()
         ret_chain = create_retrieval_chain(retriever,chain)
         stat = "OK"
         return [stat,ret_chain]
        except Exception as e:
         ret_chain = e
         stat = "error"
         return [stat,ret_chain]
           
         
