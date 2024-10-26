import streamlit as st
from chatbot import ArxivExpertChatbot

# Initialize the chatbot
chatbot = ArxivExpertChatbot('data/arxiv_dataset.csv')

# Streamlit app layout
st.title("ArXiv Expert Chatbot")
st.write("Ask me anything about computer science papers in multiple languages!")

# Text input for the user query
user_input = st.text_input("Enter your query:")

# Handle the query when the user submits input
if user_input:
    response = chatbot.handle_query(user_input)
    st.write("Chatbot:", response)
