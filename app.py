import streamlit as st


# Title
st.title("Storybot :robot_face:")
desc = '''
Bruk en språkmodell til å lage en storyline tilpasset læringsmål i ulike kurs. Språkmodellen kan hjelpe med å foreslå omgivelsene, ulike karakterer som inngår, og fremdriften i storyline'en. 
'''
st.write(desc)

with st.sidebar:
    st.sidebar.page_link('app.py', label='Hjem')
    st.sidebar.page_link('pages/storyline.py', label='Lag storyline')

if st.button('Start en storyline'):
    st.switch_page('pages/storyline.py')

