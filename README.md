# PDF RAG Summarizer

A **Retrieval-Augmented Generation (RAG)** system that allows you to **summarize PDF documents** and **ask questions about their content**.
The project combines document ingestion, vector-based retrieval, and large language models to provide concise summaries and accurate, context-aware answers.
It is designed as a **modular, extensible Python project**, suitable for coursework, research, or further development.

The system utilizes:

* **LangChain** as the orchestration framework,
* **OpenAI** for embeddings and question answering,
* **Chroma** as the vector database,
* **Transformers** for optional local PDF summarization,
* **Gradio** for a simple web-based user interface.

---

## Example

*(Screenshots can be added here once the UI is running)*

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/pdf-rag-summarizer.git
   cd PDF-summary-RAG
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your OpenAI API key:

   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

5. Prepare your documents:
   Create a `data/` directory in the project root and place your **PDF files** inside it.

6. Run the application:

   ```bash
   python app.py
   ```

7. Open your web browser and go to:

   ```
   http://localhost:7860
   ```

   to access the Gradio interface.

---

## Project Structure

```
pdf_rag_project/
├── app.py                  # Application entry point (Gradio UI)
├── config.py               # Global configuration
├── ingestion/              # PDF loading, chunking, vectorstore creation
├── summarization/          # PDF summarization logic
├── rag/                    # Retrieval and question answering
├── utils/                  # Prompts and PDF export utilities
├── data/                   # Input PDF documents
├── db/                     # Chroma vector database
└── requirements.txt
```

---

## Features

* 📄 PDF ingestion and text chunking
* 🧠 Vector-based document retrieval (RAG)
* ✍️ Automatic document summarization
* ❓ Question answering grounded in document content
* 🖥️ Simple web UI using Gradio
* 🧩 Modular architecture for easy extension

---

## Important Notes

* Only **PDF files** are supported as input documents.
* Summarization can be done:

  * locally using **Transformers** (default), or
  * via an LLM fallback if configured.
* Question answering always uses retrieved document context; if the answer is not present, the model is instructed to respond with *“I don’t know”*.
* The default language of responses depends on the document content and prompt configuration, and can be easily modified in `utils/prompts.py`.
