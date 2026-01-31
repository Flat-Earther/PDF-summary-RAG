import gradio as gr
from langchain.chat_models import init_chat_model
from config import *
from ingestion.pdf_loader import load_pdfs
from ingestion.splitter import split_documents
from ingestion.vectorstore import get_vectorstore
from summarization.transformers_sum import summarize_chunks
from summarization.llm_sum import summarize_with_llm
from rag.retriever import retrieve_chunks
from rag.qa import answer_question
from utils.pdf_export import save_summary_pdf

import os

def build_index():
    docs = load_pdfs(DATA_DIR)
    chunks = split_documents(docs, CHUNK_SIZE, CHUNK_OVERLAP)
    get_vectorstore(chunks, DB_DIR, OPENAI_EMBEDDING_MODEL)
    return "Index built successfully."

def summarize():
    docs = load_pdfs(DATA_DIR)
    chunks = [d.page_content for d in docs]
    llm = init_chat_model(OPENAI_CHAT_MODEL, model_provider="openai")

    if USE_TRANSFORMERS_SUMMARY:
        _, final = summarize_chunks(chunks, SUMMARIZER_MODEL)
    else:
        _, final = summarize_with_llm(llm, chunks)

    save_summary_pdf("summary.pdf", final)
    return final

def ask(question):
    llm = init_chat_model(OPENAI_CHAT_MODEL, model_provider="openai")
    vs = get_vectorstore([], DB_DIR, OPENAI_EMBEDDING_MODEL)
    docs = retrieve_chunks(vs, question, RETRIEVE_K)
    return answer_question(llm, docs, question)[0]

with gr.Blocks() as ui:
    gr.Markdown("# PDF RAG + Summarization System")

    gr.Button("Build Index").click(build_index, outputs=gr.Textbox())
    gr.Button("Summarize PDFs").click(summarize, outputs=gr.Textbox())

    q = gr.Textbox(label="Ask a question")
    a = gr.Textbox(label="Answer")
    gr.Button("Ask").click(ask, q, a)

ui.launch()
