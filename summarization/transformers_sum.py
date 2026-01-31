from transformers import pipeline

def summarize_chunks(chunks, model_name):
    summarizer = pipeline("summarization", model=model_name)
    chunk_summaries = []

    for c in chunks:
        res = summarizer(c, max_length=200, min_length=40, do_sample=False)
        chunk_summaries.append(res[0]["summary_text"])

    combined = "\n".join(chunk_summaries)
    final = summarizer(combined, max_length=300, min_length=80, do_sample=False)

    return chunk_summaries, final[0]["summary_text"]
