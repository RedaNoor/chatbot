import streamlit as st

# Adding title
st.title('Chatbot # 2')

st.write('Welcome to the chatbot! Please ask your question and I will try to answer it.')

# Streamlit input and output
question = st.text_input('Ask a question:', key='unique_key')

if question:
    if question.lower() == 'hello':
        st.write('Hello! How can I help you?')
    elif question.lower() == 'what is your name?':
        st.write('My name is Claude.')
    elif question.lower() == 'how are you doing today?':
        st.write("I'm doing well, thanks for asking!")
    elif question.lower() == 'how can you help me?':
        st.write("I'm an AI assistant, how can I assist you today?")
    elif question.lower() == 'what is 2 + 2?':
        st.write('2 + 2 is 4.')
    elif question.lower() == 'what color is the sky?':
        st.write('The sky is blue.')
    else:
        st.write('I am sorry, but I do not understand your question.')
