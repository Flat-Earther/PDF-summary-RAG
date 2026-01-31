from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
import os

def get_vectorstore(chunks, persist_dir, embedding_model):
    embeddings = OpenAIEmbeddings(model=embedding_model)
    if os.path.exists(persist_dir) and os.listdir(persist_dir):
        return Chroma(
            persist_directory=persist_dir,
            embedding_function=embeddings
        )
    return Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=persist_dir
    )
