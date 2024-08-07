# Importing Important Libraries
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
import bs4
class Loaders:
    def __init__(self):
       pass
         
          
    def pdfLoader(self,pdf):
       try:
         self.loader = PyPDFLoader(pdf).load()
         self.splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
         self.docs = self.splitter.split_documents(self.loader)
         self.stat = "OK"
       except Exception as e:
          self.docs = e
          self.stat = "error"
       return [self.stat,self.docs]
          
       
    def webLoader(self,web):
       try:
         self.loader = WebBaseLoader(web_paths=(web,)).load()
         self.splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
         self.docs = self.splitter.split_documents(self.loader)
         self.stat = "OK"
       except Exception as e:
          self.docs = e
          self.stat = "error"
       return [self.stat,self.docs]
   
 



       



 

 