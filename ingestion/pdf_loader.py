from langchain_core.documents import Document
from langchain_community.document_loaders.pdf import PyPDFLoader
import os

def load_pdfs(directory: str):
    documents = []
    for file in os.listdir(directory):
        if file.lower().endswith(".pdf"):
            path = os.path.join(directory, file)
            loader = PyPDFLoader(path)
            pages = loader.load()
            full_text = "\n".join(p.page_content for p in pages)
            documents.append(
                Document(
                    page_content=full_text,
                    metadata={"source_filename": file}
                )
            )
    return documents
