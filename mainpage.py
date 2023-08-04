import os

import replicate
import streamlit as st
from dotenv import load_dotenv
from elevenlabs import generate
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

load_dotenv()


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Diabites! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
     Diabites app comprises of
    (1) Personalised Intelligent Recipe Recommender based on calories, fats, and carbs
    (2) Activity Tracker Module, and 
    (3) Calorie Calculator Module.
    (4) and other assistance such as doctor recomeendation, meal recommendation etc.
"""
)

