from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI
import json

with open("models.json", 'r') as file:
    data = json.load(file)
models =data['models']
     

class Models:
    def __init__( self):
       pass
    def gpt_3_5(self):
       self.gpt35 = ChatOpenAI(model=models[0]['model'],api_key=models[0]['api-key'])
       return self.gpt35
    def gpt4o(self):
       self.gpt4o = ChatOpenAI(model=models[1]['model'],api_key=models[1]['api-key'])
       return self.gpt4o
    def llama(self):
       self.llama = ChatGroq(model=models[3]['model'],api_key=models[3]['api-key'])
       return self.llama
    def mistral(self):
       self.mistral = ChatMistralAI(model=models[4]['model'],api_key=models[4]['api-key'])
       return self.mistral
    def gemma(self):
       self.gemma = ChatGroq(model=models[5]['model'],api_key=models[5]['api-key'])
       return self.gemma
    
    
 