# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 14:56:58 2025

@author: shubh
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 23:00:31 2025

@author: shubh
"""

import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#Title and Subheader
st.title("Data Analysis")
st.subheader("Data Analysis Using Python & Streamlit!")

#Upload Dataset
upload = st.file_uploader("Upload Your Dataset (In CSV Format)")
if upload is not None:
    data = pd.read_csv(upload)
    

#Show Dataset
if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
            
#Check Datatyepe of each column
if upload is not None:
    if st.checkbox("Datatype of each column"):
        st.text("DataTypes")
        st.write(data.dtypes)
        
#Find Shape of dataset
if upload is not None:
    data_shape = st.radio("What dimension you want to Check?",("Rows", "Columns"))
    if data_shape == "Rows":
        st.text("Number of Rows")
        st.write(data.shape[0])
        
    if data_shape == "Columns":
         st.text("Number of Columns")
         st.write(data.shape[1])
         

#Find Null Values in dataset
if upload is not None:
    test = data.isnull().values.any()
    if test == True:
        if st.checkbox("Null Values in the Data"):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("Congratulations! No Missing Values.")
    
# Find Duplicate Values in Data
if upload is not None:
    test = data.duplicated().any()
    if test == True:
        st.warning("This Dataset contains Duplicate Values!")
        dup = st.selectbox("Do you want to remove Duplicate Values?",\
                           ("Select One", "Yes", "No"))
        if dup == "Yes":
            data = data.drop_duplicates()
            st.text("Duplicate Values are Removed")
        else:
            st.text("Okey! No problem.")
            
    
    
# Get Overall Statistics
if upload is not None:
    if st.checkbox("Summary of Dataset"):
        st.write(data.describe(include = 'all'))
    
    
#About section
if st.button("About App"):
    st.text("Built with Stremlit")
    st.text("Thanks to Streamlit!")


if st.checkbox("By"):
    st.success("Shubham Vidap!")
    
    
    
    
    
    
    