from dotenv import load_dotenv
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader,DirectoryLoader
from pathlib import Path

load_dotenv()

embedding_model= MistralAIEmbeddings(model='mistral-embed')

def repo_path(url):
    repo_name = url.rstrip("/").split("/")[-1]
    if repo_name.endswith(".git"):
        repo_name = repo_name[:-4]

    return {
        "name": repo_name,
        "path": Path("repositories") / repo_name
    }
    
def loadfiles(url: str):
    directoryPath= repo_path(url)["path"]

    patterns = [
    "**/*.py",
    "**/*.js",
    "**/*.ts",
    "**/*.tsx",
    "**/*.jsx",
    "**/*.html",
    "**/*.css",
    "**/*.json",
    "**/*.yaml",
    "**/*.yml",
    "**/*.toml",
    "**/*.ini",
    "**/*.env.example",
    "**/*.sql",
    "**/*.md",
    "**/*.txt",
    "**/*.dockerfile",
    "**/*.ipynb"
    ]

    docs = []

    for pattern in patterns:
        loader = DirectoryLoader(
            directoryPath,
            glob=pattern,
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"},
            silent_errors=True,
        )
        docs.extend(loader.load())
    print(f"{len(docs)} files loaded")
    return docs

def create_chunks(docs): 
    splitter= RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap= 100
    )

    chunks= splitter.split_documents(docs)
    return chunks

def create_db(chunks):
    vectorStore= FAISS.from_documents(chunks,embedding_model)
    return vectorStore.as_retriever(search_kwargs= {"k":4})

def run_db(url):
    repo_path(url)
    
    print("loadng files form repository...")
    docs= loadfiles(url)
    
    print("Creating chunks...")
    chunks= create_chunks(docs)
    
    print("Creating and sotring in database...")
    return create_db(chunks)
    
def load_context(retriever,query):
    docs= retriever.invoke(query)
    context= "\n\n".join([doc.page_content for doc in docs])
    return context 