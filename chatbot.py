# streamlit run chatbot.py

from openai import OpenAI
import streamlit as st

st.title("Storybot :robot_face:")
st.write("Velkommen til en veldig kul nettside")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


# if "openai_model" not in st.session_state:
#     st.session_state["selected_model"] = "gpt-3.5-turbo"

with st.sidebar:
    # st.title(':robot_face:')
    # st.write('Min lille chatbot')
    
    # st.subheader('Innstillinger')
    st.title('Innstillinger')
    selected_model = st.sidebar.selectbox('Velg modell', ['gpt-4', 'gpt-3.5-turbo'], key='selected_model')
    #st.session_state['selected_model'] = selected_model


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Still et spørsmål..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["selected_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})

