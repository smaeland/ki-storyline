import streamlit as st
from core import setup_chatbot


# Set up course list and description
courses = [
    'Ikke tilknytt kurs'
]

learning_outcomes = {}
for course in courses:

    if course == 'Ikke tilknytt kurs':
        learning_outcomes[course] = '(ingen læringsmål)'
    else:
        with open(f'courses/{course}.md', 'r') as fin:
            learning_outcomes[course] = fin.read()


prompt = '''
Du er en assistent som skal hjelpe med å lage en storyline, etter den skotske
storyline-modellen for interaktiv undervisning. Målgruppen er barn i barnehage.
Her er læringsmålene som vår storyline bør inneholde: 
'''

setup_chatbot(prompt, courses)
