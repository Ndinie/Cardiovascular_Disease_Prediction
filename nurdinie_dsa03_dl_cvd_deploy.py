# -*- coding: utf-8 -*-
"""NURDINIE_DSA03_DL_CVD_deploy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vLzsmuMbUoOwS96o78blva7gbLTwb1QY

STREAMLIT

REFER:

[Run streamlit app from a Google Colab Notebook](https://colab.research.google.com/github/mrm8488/shared_colab_notebooks/blob/master/Create_streamlit_app.ipynb#scrollTo=IFvZnzS4vr88)
"""

!pip install -q streamlit

!pip install pyngrok

!ngrok authtoken 2CCdOwNmmCHIe3WlX5xAxwDzzA1_5HZEjjf3v8f9c9zA7iHm1

!wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip

!unzip ngrok-stable-linux-amd64.zip

from pyngrok import ngrok 
public_url = ngrok.connect(port='8501')
public_url

# import subprocess
# import sys
# import streamlit as st
# @st.cache
# def install(package):
#     subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
# install('pickle-mixin')
# install('sklearn')

"""Deployment"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile DSA03_DL_streamlit_app.py 
# import subprocess
# import sys
# import streamlit as st
# @st.cache
# def install(package):
#     subprocess.check_call([sys.executable, "-m", "pip", "install", package])
#     
# install('pickle-mixin')
# install('sklearn')
# 
# # testing form
# import os
# import pickle
# import pandas as pd
# import numpy as np
# import streamlit as st
# 
# MODEL_PATH = os.path.join(os.getcwd(), 'best_estimator.pkl')
# with open(MODEL_PATH, 'rb') as file:
#   model = pickle.load(file)
# 
# with st.form("Heart Attack Predictor App"):
#     chol=st.selectbox('Cholesterol Level: 1: normal, 2: above normal, 3: well above normal',(1,2,3))
#     sys=st.number_input('Systolic BP')
#     dia=st.number_input('Diastolic BP')
# 
#     # Every form must have a submit button.
#     submitted = st.form_submit_button("Submit")
#     if submitted:
#         new_data=np.expand_dims([chol,sys,dia],axis=0)
#         outcome=model.predict(new_data)[0]
# 
#         if outcome==0:
#             st.write('Congrats! You are healthy!!')
#             st.balloons()
#         else:
#             st.write('Thats not good, You need to start exercising!!')
#             st.snow()

!streamlit run /content/DSA03_DL_streamlit_app.py & npx localtunnel -p 8501

