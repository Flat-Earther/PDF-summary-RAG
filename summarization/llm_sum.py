def summarize_with_llm(llm, chunks):
    chunk_summaries = []
    for c in chunks:
        out = llm.invoke(
            "Summarize this text briefly:\n\n" + c
        )
        chunk_summaries.append(out.content)

    final = llm.invoke(
        "Combine these summaries into one coherent summary:\n\n"
        + "\n".join(chunk_summaries)
    )
    return chunk_summaries, final.content
