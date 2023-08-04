import os
import streamlit as st
from dotenv import load_dotenv

from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

from importlib.resources import contents
from random import choices

from streamlit_chat import message
import openai


#llm = OpenAI(temperature=0.9)

#openai_api_key = os.getenv("OPENAI_API_KEY")
#eleven_api_key = os.getenv("ELEVEN_API_KEY")

st.set_page_config(
   page_title="Activity Tracker",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.markdown("# Activity Tracker ")
st.sidebar.header(" Activity Tracker ")
st.write(
    """  
    This module uses the knowledge-based approach, and tracks the activities of user based on live tracker 
    """
)

load_dotenv()

def generate_response(text):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": text},
        
        ]
    )
    return response['choices'][0]['message']['content']
    

def get_text():
    input_text = st.text_input("", key = "input_text")
    return input_text


if 'past' not in st.session_state:
    st.session_state['past'] = [] ## user generated text

if 'generated' not in st.session_state:
    st.session_state['generated'] = [] ## AI generated text



def main():
    #st.title('My Meal Recommender Bot')
    user_input = get_text()

    if user_input:
        response = generate_response(user_input)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(response)

    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user='True')
            message(st.session_state['generated'][i])
    
if __name__ == '__main__' :
    main()
    