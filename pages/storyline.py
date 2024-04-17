import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


# Set up course list and description
courses = [
    'MGBNA101',
    'Ikke tilknytt kurs'
]

learning_outcomes = {}
for course in courses:

    if course == 'Ikke tilknytt kurs':
        learning_outcomes[course] = '(ingen læringsmål)'
    else:
        with open(f'courses/{course}.md', 'r') as fin:
            learning_outcomes[course] = fin.read()


# print('learning_outcomes:')
# for k in learning_outcomes:
    # print(k, ':', learning_outcomes[k][:20])


# Sidebar
with st.sidebar:
    st.sidebar.page_link('app.py', label='Hjem')
    st.sidebar.page_link('pages/storyline.py', label='Lag storyline')

    st.title('Innstillinger')
    gpt_model = st.sidebar.selectbox('Velg modell', ['gpt-4', 'gpt-3.5-turbo'], key='gpt_model')

# Course selector
selected_course = st.selectbox(
    'Velg kurs',
    ('MGBNA101', 'Ikke tilknytt kurs')
)

with st.expander('Se læringsmål'):
    st.markdown(learning_outcomes[selected_course])

# If chat has not started yet, insert the chosen learning outcome description
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append(
        {
            'role': 'user',
            'content': learning_outcomes[selected_course]
        }
    )

# Show messages (but not the initial description)
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat 
if prompt := st.chat_input("Still et spørsmål..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["gpt_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})

    # print(st.session_state.messages)

