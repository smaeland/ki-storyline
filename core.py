import streamlit as st
from openai import OpenAI


def setup_api_client() -> OpenAI:

    if not 'client' in vars():
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    else:
        print('client OK')

    return client
    

def load_learning_outcomes(course_list: list[str]) -> dict[str, str]:
     
    texts = {}
    for course in course_list:

        if course == 'Ikke tilknytt kurs' or course is None:
            texts[course] = '(ingen læringsmål)'
        else:
            with open(f'courses/{course}.md', 'r') as fin:
                texts[course] = fin.read()

    return texts


def setup_chatbot(init_prompt: str, course_list: list[str]):
    '''
    Set up course selection and chatbot, same for all subpages 
    '''

    client = setup_api_client()

    # Load course descriptions
    learning_outcomes = load_learning_outcomes(course_list)
    
    # Request user to reload if changing courses midway
    def warn_reload():
        if 'messages' in st.session_state and len(st.session_state.messages) > 1:
            st.warning('Last inn siden på ny for å bytte kurs. OBS! Dette sletter samtalen så langt.')

            
    # Sidebar
    st.sidebar.header('Innstillinger')
    st.sidebar.selectbox(
        'Velg modell', 
        ['gpt-4', 'gpt-3.5-turbo'],
        key='gpt_model'
    )

    # Tips, currently does nothing :/
    st.sidebar.header('Tips')
    st.sidebar.write('Skriv inn en melding, eller bruk et av disse forslagene:')
    suggestions = [
        'Foreslå en omgivelse for storylinen',
        'Foreslå karakterer som deltar',
        'Foreslå en hendelse som driver historien fremover'
    ]
    for suggestion in suggestions:
        if st.sidebar.button(
            label=suggestion,
        ):
            pass

    # Course selector
    selected_course = st.selectbox(
        'Velg kurs',
        course_list,
        on_change=warn_reload

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
