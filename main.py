from embeddings.embeddings import embeddings
from LLM.llm import Models
from ways.agent import AgentExecutorWrapper
from ways.retrieval_chain import retrival_chain
from vector_db.vector_database import vector_db
from loaders.Loaders import Loaders
import json
import streamlit as st
from streamlit_chat import message
from langchain_core.load import dumpd, dumps, load, loads
 
# Page configuration
st.set_page_config(
    page_title="RAG Chatbot",
    page_icon=":robot:",
    layout="centered",
    initial_sidebar_state="auto",
)

# CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #001f3f;
        color: white;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
        border-radius: 12px;
    }
    .stButton>button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
    .navbar-container {
        display: flex;
        justify-content: flex-end;
        gap: 10px;
        position: fixed;
        top: 10px;
        right: 10px;
        background-color: #001f3f;
        padding: 10px;
        border-radius: 10px;
        z-index: 1000;
    }
    .navbar-container select {
        font-size: 12px;
        padding: 5px;
        border-radius: 5px;
        width: 150px;
    }
    .input-container {
        display: flex;
        justify-content: center;
        gap: 10px;
        position: fixed;
        bottom: 10px;
        width: 100%;
        padding: 10px;
        background-color: #001f3f;
        border-radius: 10px;
    }
    .input-container input {
        background-color: #001f3f;
        color: white;
        border: 2px solid #4CAF50;
        border-radius: 5px;
        padding: 10px;
        width: 80%;
    }
    .pdf-url-container {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-top: 10px;
    }
    .pdf-url-container input {
        background-color: #001f3f;
        color: white;
        border: 2px solid #4CAF50;
        border-radius: 5px;
        padding: 10px;
        width: 80%;
    }
    .stMarkdown h1 , .stMarkdown h3 {
        color: white;
    }
    .stMarkdown h2{
        color: red;
    }
    .message-container {
        background-color: #001f3f;
        color: white;
        border: 1px solid #4CAF50;
        border-radius: 5px;
        padding: 10px;
        margin-bottom: 5px;
        display: flex;
        align-items: center;
    }
    .message-container.bot {
        border-left: 4px solid #4CAF50;
        justify-content: flex-start;
    }
    .message-container.user {
        border-right: 4px solid #4CAF50;
        justify-content: flex-end;
        text-align: right;
    }
    .message-container img {
        border-radius: 50%;
        width: 40px;
        height: 40px;
        margin: 0 10px;
    }
    .message-container.user img {
        order: 2;
    }
    .message-container.bot img {
        order: 1;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Error handling variable
Error = ""
 

 

# Function to set up vector database
def Vector_db():
    global Error
    try:
        # Save PDF to a temporary file
        if input_type == "PDF":
            with open("temp.pdf", "wb") as f:
                f.write(pdf_file.getbuffer())
                
        # Load documents
        if input_type == "Webpage":
            docs = Loaders().webLoader(webpage_url)
            print(docs)
        elif input_type == "PDF":
            docs = Loaders().pdfLoader("temp.pdf")
            print(docs)
            
        # Handle errors
        if docs[0] == "error":
            Error = docs[1]
            return None
        
        # Set up embeddings
         
        Embeddings = embeddings().google()
         
        
        # Set up vector database
        if vector_databases == "objectbox":
            vector_database = vector_db(Embeddings, docs[1]).objectBox()
        elif vector_databases == "Faiss":
            vector_database = vector_db(Embeddings, docs[1]).Faiss()
        elif vector_databases == "Chroma":
            vector_database = vector_db(Embeddings, docs[1]).chroma()
        
        print(vector_database)
        # Handle vector database setup errors
        if vector_database[0] == "error":
            Error = vector_database[1]
             
            return None
        elif vector_database[0 ] == "OK":
            return vector_database[1]
    except Exception as e:
        Error = str(e)
        print(e)
        return None

# Function to set up agent or retrieval chain
def agent(vector):
    global Error
    try:
        # Load model configuration
        with open('models.json', 'r') as model:
            data = json.load(model)
        cse_id, Api_Keys = data['apis'][4]['Google-Cse-Id'], data['apis'][0]['google-api-key']
        
        # Set up LLM model
        if llm_model == "gpt-3.5-turbo":
            llm = Models().gpt_3_5()
        elif llm_model == "gpt-4o-mini":
            llm = Models().gpt4o()
        elif llm_model == "llama3-70b-8192":
            llm = Models().llama()
        elif llm_model == "mistral-large-2407":
            llm = Models().mistral()
        elif llm_model == "gemma2-9b-it":
            llm = Models().gemma()
        
        # Set up chain or agent
        if chain_type == "Agentic":
            chain = AgentExecutorWrapper.create_agent(llm, vector, Api_Keys, cse_id)
        elif chain_type == "Retrieval":
            chain = retrival_chain.create_chain(llm, vector)
        print(chain)
        # Handle chain setup errors
        if chain[0] == "error":
            Error = chain[1]
            return None
        else:
            return chain[1]
    except Exception as e:
        Error = str(e)
        return None

# Function to predict answer
def predict_answer():
    global Error
    try:
        # Predict answer based on chain type
        if chain_type == "Agentic":
            answer = st.session_state.type.invoke({'input': user_input})
            return answer['output']
        elif chain_type == "Retrieval":
            answer = st.session_state.type.invoke({'input': user_input})
            return answer['answer']
    except Exception as e:
        Error = str(e)
        return None

# Title and description
st.markdown("# Welcome to the RAG-CHAT", unsafe_allow_html=True)
st.markdown("### Your intelligent assistant powered by Retrieval-Augmented Generation", unsafe_allow_html=True)

# Input, embeddings, and vector database
st.markdown("<div class='navbar-container'>", unsafe_allow_html=True)
input_type = st.selectbox("Select Input Type", ["Webpage", "PDF"], index=0, key="input_type")
embeddings_model = st.selectbox("Select Embeddings Model", ["text-embedding-3-small"], index=0, key="embeddings")
vector_databases = st.selectbox("Select Vector Database", ["Faiss", "Chroma","objectbox"], index=0, key="vector_db")
st.markdown("</div>", unsafe_allow_html=True)

# Checking if input is PDF or webpage
st.markdown("<div class='pdf-url-container'>", unsafe_allow_html=True)
if input_type == "PDF":
    pdf_file = st.file_uploader("Upload PDF", type=["pdf"], key="pdf_upload")
elif input_type == "Webpage":
    webpage_url = st.text_input("Enter URL:", key="webpage_url", placeholder="Enter the URL of the webpage")
st.markdown("</div>", unsafe_allow_html=True)

 

 
# Vector database setting up button
if st.button('Make Vector Database'):
    if input_type:
         
        st.session_state.vectordb = Vector_db()
        
        if st.session_state.vectordb:
            st.success("Successfully made Vector Database.")
            print(st.session_state.vectordb)
            
            
        else:
            st.error("Failed to create Vector Database. " + Error)
             
    else:
        st.error("Please provide data either in the form of a PDF or a webpage.")
 
  
# LLM model and chain setup
llm_model = st.selectbox("Select LLM Model", ["gpt-3.5-turbo" , "gpt-4o-mini", "llama3-70b-8192", "mistral-large-2407", "gemma2-9b-it"], index=0, key="llm_model")
chain_type = st.selectbox("Select Chain Type", ["Agentic", "Retrieval"], index=0, key="chain_type")

# Chain or agent setup 


if st.button('Setup Chain/Agent'):
  
    if st.session_state.vectordb:
        st.session_state.type = agent(st.session_state.vectordb)
        if st.session_state.type:
            st.success("Successfully set up Chain/Agent.")
        else:
            st.error("Failed to set up Chain/Agent. " + Error)
    else:
        st.error("Please create a Vector Database first.")

 
    


# Input for user query
st.markdown("<div class='input-container'>", unsafe_allow_html=True)
user_input = st.text_input("Ask a question:", key="user_input", placeholder="Type your question here...")
submit_button = st.button('Submit', key="submit_button")
st.markdown("</div>", unsafe_allow_html=True)

# Displaying chat messages
if submit_button:
  if st.session_state.type:
    if user_input:
        answer = predict_answer()
        if answer:
            st.write(f"<div class='message-container user'><img src='https://via.placeholder.com/40' alt='User'/> {user_input}</div>", unsafe_allow_html=True)
            st.write(answer, unsafe_allow_html=True)
        else:
            st.error("Failed to get an answer. " + Error)
    else:
        st.error("Please enter a question.")
  else:
      st.error("No, document retreival chain or agent founded!")

# Error handling
if Error:
    st.error(f"An error occurred: {Error}")

# Clear the error after displaying
Error = ""


