from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores import Chroma
from langchain_community.vectorstores import Cassandra
from langchain_objectbox.vectorstores import ObjectBox

class vector_db:
    def __init__(self, embedding,docs):
        self.embedding = embedding
        self.docs = docs
        pass
    def chroma(self):
        try:
            self.chromA= Chroma.from_documents(self.docs,self.embedding)
            self.status ="OK"
        except Exception as e:
            self.chromA = e
            self.status = "ERROR"
        return [self.status,self.chromA]
     
    def Faiss(self):
        try:
            self.faiss= FAISS.from_documents(self.docs,self.embedding)
            self.status ="OK"
        except Exception as e:
            self.faiss = e
            self.status = "ERROR"
        return [self.status,self.faiss]
    def objectBox(self):
        try:
            self.objectbox= ObjectBox.from_documents(self.docs,self.embedding,embedding_dimensions=768)
            self.status ="OK"
        except Exception as e:
            self.objectbox = e
            self.status = "ERROR"
        return [self.status,self.objectbox]

  