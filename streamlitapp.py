import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file,get_table_data
from src.mcqgenerator.logger import logging

#imporing necessary packages packages from langchain
from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

from src.mcqgenerator.logger import logging
from src.mcqgenerator.MCQGenerator import GenerateChain
import streamlit as st

# Importing JSON
with open("C:\\Users\\HP\\MCQGenerator\\Response.json","r") as file:
    RESPONSE_JSON = json.load(file)

# Creating a title for the app
st.title("MCQs Creator Application with LangChain")
#Create a form using st.form 
with st.form("user_inputs"):
    #File Upload
    uploaded_file=st.file_uploader("Uplaod a PDF or txt file")
    #Input Fields
    mcq_count=st.number_input("No. of MCQs", min_value=3, max_value=50)
    #Subject
    subject=st.text_input("Insert Subject", max_chars=20)
    # Quiz Tone
    tone=st.text_input("Complexity Level Of Questions", max_chars=20, placeholder="Simple")
    #Add Button
    button=st.form_submit_button("Create MCQs")
    # Check if the button is clicked and all fields have input
    if button and uploaded_file is not None and mcq_count and subject and tone: 
        with st.spinner("loading..."):
            try:
                text=read_file(uploaded_file)
                response=GenerateChain(text, mcq_count, subject, tone, RESPONSE_JSON)
                # st.write(response)
            except Exception as e:
                traceback.print_exception (type (e), e, e.__traceback__)
                print("Error", e)
                st.error("Error")

            else:
    
                if isinstance (response, dict):
                    #Extract the quiz data from the response 
                    quiz = response.get("quiz", None)
                    if quiz is not None:
                        table_data=get_table_data(quiz)
                        print(table_data) 
                        if table_data is not None:
                            df=pd.DataFrame(table_data) 
                            df.index=df.index+1
                            st.table(df)
                            #Display the review in atext box as well 
                            st.text_area(label="Review", value=response["review"])
                        else:
                            st.error("Error in the table data")
                    else:
                        st.write(response)