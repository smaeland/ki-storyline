import streamlit as st

st.set_page_config(page_title='Hjem', page_icon='🤖')



# Title
st.title("Storybot :robot_face:")
desc = '''
Bruk en språkmodell til å lage en storyline tilpasset læringsmål i ulike kurs.
Språkmodellen kan hjelpe med å foreslå omgivelsene, ulike karakterer som
inngår, og fremdriften i storyline'en. 
'''
st.write(desc)

#with st.sidebar:
#    st.sidebar.page_link('app.py', label='Hjem')
#    st.sidebar.page_link('pages/storyline.py', label='Lag storyline')


st.subheader('Lag en storyline ved å velge retning:')

if st.button('Grunnskolelærer 1.-7. trinn'):
    st.switch_page('pages/GRU.py')

if st.button('Barnehagelærer'):
    st.switch_page('pages/BLU.py')
