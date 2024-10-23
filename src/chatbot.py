from src.extract import extract_info
from src.summarizer import summarize_text
from src.explain_llm import generate_explanation

def handle_query(query):
    """Handle user queries and return a comprehensive response."""
    
    info = extract_info(query)

    summary = summarize_text(info)

    explanation = generate_explanation(query, summary)

    response = f"Summary:\n{summary}\n\nExplanation:\n{explanation}"
    return response
