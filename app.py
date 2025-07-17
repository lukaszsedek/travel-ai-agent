import streamlit as st
from agent import run_agent

st.set_page_config(page_title="🌍 Smart Travel Buddy Chat")
st.title("🌍 Smart Travel Buddy")

# Inicjalizacja historii czatu
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Widok czatu
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Wprowadzenie przez użytkownika
user_input = st.chat_input("Dokąd chcesz pojechać?")

if user_input:
    # Dodaj pytanie użytkownika do historii
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Myślę..."):
            response = run_agent(user_input, st.session_state.chat_history)
            st.markdown(response)

    # Dodaj odpowiedź AI do historii
    st.session_state.chat_history.append({"role": "assistant", "content": response})
