Here's an updated README.md file with additional instructions for adding API keys for all LLMs and mentioning the requirements.txt file installation.

markdown
Copy code
# RAG-CHAT

Welcome to the RAG Chatbot project! This project is a Streamlit-based intelligent assistant powered by Retrieval-Augmented Generation (RAG). It leverages multiple Large Language Models (LLMs), embedding models, and vector databases to provide insightful answers from documents or web pages.

## Features

- **LLM Models Used**: 
  - gemma2 90b
  - mistral large 2407
  - llama3 70b
  - chat gpt 3.5 turbo
  - chat gpt 4o mini
- **Embedding Models**: 
  - text-embedding-3-small
  - Google Palm Embeddings
- **Vector Databases**: 
  - FAISS
  - Chroma
  - Object Box
- **Ways to Retrieve Information**: 
  - Agent
  - Document Retrieval Chain
- **Input Types**: 
  - PDF
  - Web Page

## Getting Started

To get started with the RAG Chatbot, follow these steps:

### Prerequisites

- Python 3.8 or higher
- Streamlit
- Install the required Python libraries:
  ```bash
  pip install -r requirements.txt
Setup
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/rag-chatbot.git
cd rag-chatbot
Create and Configure models.json File:
Add your API keys in the models.json file. Here is an example structure:

json
Copy code
{
  "apis": [
    {"google-api-key": "your-google-api-key"},
    {"Google-Cse-Id": "your-google-cse-id"},
    {"gemma2-api-key": "your-gemma2-api-key"},
    {"mistral-api-key": "your-mistral-api-key"},
    {"llama3-api-key": "your-llama3-api-key"},
    {"chat-gpt-3.5-api-key": "your-chat-gpt-3.5-api-key"},
    {"chat-gpt-4o-api-key": "your-chat-gpt-4o-api-key"}
  ]
}
Run the Application:

bash
Copy code
streamlit run app.py
Usage
User Interface
Navbar: Located at the top right, select the input type (PDF or Webpage), embeddings model, and vector database.
Input Section:
If PDF is selected, upload your PDF file.
If Webpage is selected, enter the URL of the webpage.
Vector Database Setup: Click Make Vector Database to create the vector database.
LLM and Chain Setup: Choose the LLM model and chain type, then click Setup Chain/Agent.
Query Input: Type your question and click Submit.
Code Structure
embeddings/embeddings.py: Embedding models implementation.
LLM/llm.py: Large Language Models implementation.
ways/agent.py: Agent executor wrapper.
ways/retrieval_chain.py: Retrieval chain implementation.
vector_db/vector_database.py: Vector database implementation.
loaders/Loaders.py: PDF and web page loaders.
app.py: Main Streamlit application file.
Customization
You can customize the chatbot by adding new models, changing the UI, or modifying the retrieval methods. The code is modular and can be easily extended.

Adding New Models
Define the Model in LLM/llm.py.
Update the UI to include the new model in the dropdown options.
Error Handling
The app includes comprehensive error handling to ensure smooth user experience. Errors are displayed at the bottom of the page, and successful operations trigger popups for user feedback.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

License
This project is licensed under the MIT License.

Acknowledgements
Streamlit
Langchain
Google API
Contact
For any questions, feel free to reach out at [arorahardik344@gmail.com].

 

This `README.md` file now includes instructions to install dependencies from the `requirement.txt'