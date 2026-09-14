from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

def cargar_documentos(ruta: str):
    documentos = []
    for archivo in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, archivo)
        if archivo.endswith(".txt"):
            loader = TextLoader(ruta_completa, encoding="utf-8")
            documentos.extend(loader.load())
        elif archivo.endswith(".pdf"):
            loader = PyPDFLoader(ruta_completa)
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

    prompt = ChatPromptTemplate.from_messages([
        ("system", """Eres un asistente de atención al cliente profesional.
        Responde usando solo la información del contexto proporcionado.
        Si no tienes la información, dilo claramente.
        Contexto: {context}"""),
        MessagesPlaceholder(variable_name="historial"),
        ("human", "{question}")
    ])

    def obtener_contexto(input):
        return retriever.invoke(input["question"])

    cadena = (
        {
            "context": obtener_contexto,
            "historial": lambda x: x["historial"],
            "question": lambda x: x["question"]
        }
        | prompt
        | llm
        | StrOutputParser()
    )
    return cadena