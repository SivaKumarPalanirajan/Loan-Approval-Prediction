import pandas as pd 
import numpy as np 
import streamlit as st
import base64
from sklearn.metrics import accuracy_score

@st.cache_data()
def get_base64_of_bin_file(file):
    with open(file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
pic=get_base64_of_bin_file("bg7.png")
st.title("Loan Approval Predictor")
page_bg_img = f'''
    <style>
    .stApp {{
    background-image: url("data:image/png;base64,{pic}");
    background-size: cover;
    }}
    </style>
    '''
st.markdown(page_bg_img, unsafe_allow_html=True)
st.info("ENTER DETAILS BELOW")

#getting in the input

loan_term=st.number_input("Enter Loan Term:")
cibil_score=st.number_input("Enter CIBIL Score:")

confirmation=st.text_input("PLEASE ENTER CONFIRM IF THE DETAILS ARE CORRECT")
L=[loan_term,cibil_score]

if confirmation!="":
    import pickle
    model= pickle.load(open('models/RandomForestModel.sav', 'rb')) 
    y_pred=model.predict([L])
    st.write("ACCORDING TO OUR MODEL'S PREDICTION:")
    y_pred=y_pred[0]
    print(y_pred)
    st.markdown(f"Your Loan is predicted to be {y_pred}")
else:
    st.stop()
