# app/main.py

import streamlit as st
from supervisoragent import build_agent

agent = build_agent()

st.title("Agentic AI Chatbot 🤖")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask anything...")

if user_input:
    response = agent.run(user_input)

    st.session_state.messages.append(("user", user_input))
    st.session_state.messages.append(("assistant", response))

for role, msg in st.session_state.messages:
    st.chat_message(role).write(msg)