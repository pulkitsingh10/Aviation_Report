import streamlit as st
import pandas as pd

st.image("assets/india-airports-map.png")

st.header("Total Passengers Movements")

df1 = pd.read_excel("assets/Mar2k24Annex3 (1).xlsx",
                    sheet_name="Table 4",
                    engine="openpyxl",
                    skiprows=2
                    )

st.dataframe(df1)

st.header("Total Aircrafts Movements")

df2 = pd.read_excel("assets/Mar2k24Annex2 2.xlsx",
                    sheet_name="Table 4",
                    engine="openpyxl",
                    skiprows=2
                    )

st.dataframe(df2)
