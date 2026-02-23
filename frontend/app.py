import streamlit as st
import requests

st.title("sonu")

user_input = st.text_input("Ask something:")

if st.button("Send"):
    response = requests.post(
        "http://127.0.0.1:5000/chat",
        json={"message": user_input}
    )

    st.write("Bot:", response.json()["response"])