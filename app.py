import streamlit as st
from src.chatbot import handle_query

st.title("arXiv Expert Chatbot")


query = st.text_input("Enter your query:")

if st.button("Submit"):
    if query:
        response = handle_query(query)
        st.text_area("Response", response, height=300)
    else:
        st.warning("Please enter a query.")
