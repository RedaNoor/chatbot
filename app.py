import streamlit as st

# Adding title
st.title('Chatbot')

st.write('Welcome to the chatbot! Please do ask your question and I will try to answer it.')

question = st.text_input('Ask a question:', key='unique_key')

while question == 'goodbye':
    st.write('Goodbye! Have a nice day!')
    break

if question == 'hello':
    st.write('Hello! How can I help you?')
elif question == 'what is your name?':
    st.write('name')
elif question == 'Hi, I am a Practice Chatbot':
    st.write("I'm doing well, thanks for asking!")
elif question == 'help':
    st.write("I am an AI assistant, how can I assist you today?")
elif question == '2+2':
    st.write('2 + 2 is 4.')
elif question == '3+3':
    st.write('3 + 3 is 6.')
elif question == '4+4':
    st.write('4 + 4 is 8.')
elif question == '5+5':
    st.write('5 + 5 is 10.')
elif question == '6+6':
    st.write('6 + 6 is 12.')
elif question == '7+7':
    st.write('7 + 7 is 14.')
elif question == '8+8':
    st.write('8 + 8 is 16.')
elif question == '9+9':
    st.write('9 + 9 is 18.')
elif question == '10+10':
    st.write('10 + 10 is 20.')
elif question == '9*1':
    st.write('9 * 1 is 9.')
elif question == '9*2':
    st.write('9 * 2 is 18.')
elif question == '9*3':
    st.write('9 * 3 is 27.')
elif question == '9*4':
    st.write('9 * 4 is 36.')
elif question == '9*5':
    st.write('9 * 5 is 45.')
elif question == '9*6':
    st.write('9 * 6 is 54.')
elif question == '9*7':
    st.write('9 * 7 is 63.')
elif question == '9*8':
    st.write('9 * 8 is 72.')
elif question == '9*9':
    st.write('9 * 9 is 81.')
elif question == '9*10':
    st.write('9 * 10 is 90.')
elif question == 'what color is the sky?':
    st.write('The sky is blue.')
elif question == 'goodbye':
    st.write('Goodbye! Have a nice day!')
else:
    st.write('I am sorry, but I do not understand your question.')
