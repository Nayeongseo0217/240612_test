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
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
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
        st.markdown(assistant_message)
        st.session_state.messages.append({"role": "assistant", "content": assistant_message})
