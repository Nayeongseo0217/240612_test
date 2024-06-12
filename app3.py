import openai
import streamlit as st

st.title("오토커넥트 챗봇")

# OpenAI API 키 설정
api_key = st.secrets["OPENAI_API_KEY"]
openai.api_key = api_key

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"  # 적절한 엔진을 선택해주세요.

system_message = '''
'''

if "messages" not in st.session_state:
    st.session_state.messages = []

if len(st.session_state.messages) == 0:
    st.session_state.messages.append({"role": "system", "content": system_message})

for idx, message in enumerate(st.session_state.messages):
    if idx > 0:
        role = "User" if message["role"] == "user" else "Assistant"
        st.markdown(f"**{role}:** {message['content']}")

prompt = st.text_input("What is up?")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f"**User:** {prompt}")

    response = openai.ChatCompletion.create(
        model=st.session_state["openai_model"],
        messages=st.session_state.messages,
        temperature=0.7,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    assistant_message = response.choices[0].message["content"].strip()
    st.markdown(f"**Assistant:** {assistant_message}")
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})

# Clear the input box after submission
st.text_input("What is up?", value="", key="chat_input")
