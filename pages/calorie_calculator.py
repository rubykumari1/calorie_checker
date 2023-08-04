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



st.set_page_config(
   page_title="Calorie Calculator",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.markdown("# Calorie Calculator ")
st.sidebar.header(" Calorie Calculator")
st.write(
    """  This module calculates the BMI index and other relevant determinants
    """
)

load_dotenv()

col1,col2,col3,col4 = st.columns([1,2,3,4])
col1.title('BMI:')
col3.title('Glucose Readings:')

with st.form('BMI Index Calculator'):
    glucose_readings = st.number_input('log blood glucose readings')
    body_weight = st.number_input('body_weight')
    height = st.number_input('height')
    
    submit = st.form_submit_button('calculate')

if submit:
    col2.title(f'{(body_weight/height):.2f}')
    col4.title(f'{glucose_readings: .2f}')



def main():
    pass
   
    
if __name__ == '__main__' :
    main()
    