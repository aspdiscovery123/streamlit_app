# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:07:55 2024

@author: Admin
"""


import json
import streamlit as st
import requests


server ='http://4.156.167.137:5000'

st.title("Bank Application")

st.write("Enter value to perform testing")

cc = st.number_input("Credit Score",step=1)
age = st.number_input("Age",step=1)
geo = st.text_input("Geography")
gen = st.text_input("Gender")
balance = st.number_input("Balance",step=0.11)
n_p= st.number_input("Number of Product",step=1)
is_active=st.number_input("Is Active Member",step=1)

if st.button("Submit"):
    data={
        "CreditScore":cc,
      "Geography":geo,
      "Gender":gen,
      "Age":age,
      "Balance":balance,
      "NumOfProducts":n_p,
      "IsActiveMember":is_active
        }
    data={"info":data}
    data=json.dumps(data)
    print(data)
    
    r=requests.post(server,data)
    if r.status_code==200:
        print(r.content)
        st.success({"prediction":str(r.content)})
    else:
        st.error("not working")
    
    
    
    

    
    

