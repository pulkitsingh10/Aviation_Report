import streamlit as st
import pandas as pd 
import plotly.express as px

st.title("Profit Table")
st.subheader("Upload your excel file")

uploaded_file=st.file_uploader('Choose a XLSX file', type='xlsx')
if uploaded_file:
    st.markdown('---')
    df=pd.read_excel(uploaded_file,
                     #engine='openpyxl',
                     skiprows=6,
                     nrows=1000
    )
    st.dataframe(df)