from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
import os

load_dotenv()



def cargar_documentos(ruta: str):
    documentos = []
    for archivo in os.listdir(ruta):
        if archivo.endswith(".txt"):
            ruta_completa = os.path.join(ruta, archivo)
            loader = TextLoader(ruta_completa, encoding="utf-8")
            documentos.extend(loader.load())
    return documentos

def crear_vectorstore(documentos):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    fragmentos = splitter.split_documents(documentos)
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(fragmentos, embeddings)
    return vectorstore

def crear_cadena_rag(vectorstore):
    llm = ChatOpenAI(model="gpt-4", temperature=0)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    prompt = ChatPromptTemplate.from_template("""
    Eres un asistente de atención al cliente. Responde usando solo la información proporcionada.
    Si no sabes la respuesta, di que no tienes esa información.

    Contexto: {context}
    Pregunta: {question}
    """)

    cadena = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return cadena