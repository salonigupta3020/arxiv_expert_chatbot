from transformers import pipeline

def summarize_text(text):
    """Summarizes the given text."""
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']
