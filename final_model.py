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
married = st.radio("ARE YOU MARRIED:",["Yes","No"])
employed=st.radio("ARE YOU SELF EMPLOYED:",["Yes","No"])
history=st.number_input("ENTER CREDIT HISTORY:")
area=st.radio("ENTER THE AREA OF THE PROPERTY:",["Urban","Rural","Semiurban"])
confirmation=st.text_input("PLEASE ENTER CONFIRM IF THE DETAILS ARE CORRECT")
L=[married,employed,history,area]
df1=pd.DataFrame(L)
df1[0]=np.where(df1[0]=="No",0,df1[0])
df1[0]=np.where(df1[0]=="Yes",1,df1[0])
df1[0]=np.where(df1[0]=="Urban",2,df1[0])
df1[0]=np.where(df1[0]=="Rural",0,df1[0])
df1[0]=np.where(df1[0]=="Semiurban",1,df1[0])
df1=df1.T

if confirmation!="":
    print(df1)
    import pickle
    model= pickle.load(open('model.sav', 'rb')) 
    y_pred=model.predict(df1)
    st.write("ACCORDING TO OUR MODEL'S PREDICTION:")
    if y_pred==1:
        print("LOAN APPROVED")
        st.markdown("LOAN APPROVED")
    else:
        print("LOAN NOT APPROVED")
        st.markdown("LOAN NOT APPROVED")

else:
    st.stop()
