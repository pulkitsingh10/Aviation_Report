import streamlit as st
import pandas as pd

st.header("List of RCS Routes Commenced Under RCS-UDAAN 1.0, 2.0, 3.0, 4.0, 4.1, 4.2, 4.3, 5.0, 5.1 and 5.3")

selected = st.selectbox(
    'Select', [1.0, 2.0, 3.0, 4.0, 4.1, 4.2, 4.3, 5.0, 5.1, 5.3])

if selected == 1.0:
    df = pd.read_excel("assets/579 RCS Routes Operationalised as on 08.07.2024.xlsx",
                       sheet_name="Table 1",

                       )
    st.dataframe(df)

elif selected == 2.0:
    df = pd.read_excel("assets/579 RCS Routes Operationalised as on 08.07.2024.xlsx",
                       sheet_name="Table 2",
                       # engine="openpyxl",
                       skiprows=1
                       )
    st.dataframe(df)

elif selected == 3.0:
    df = pd.read_excel("assets/579 RCS Routes Operationalised as on 08.07.2024.xlsx",
                       sheet_name="Table 3",
                       # engine="openpyxl",
                       skiprows=1
                       )
    st.dataframe(df)

elif selected == 4.0:
    df = pd.read_excel("assets/579 RCS Routes Operationalised as on 08.07.2024.xlsx",
                       sheet_name="Table 4",
                       # engine="openpyxl"
                       )
    st.dataframe(df)

elif selected == 4.1:
    df = pd.read_excel("assets/579 RCS Routes Operationalised as on 08.07.2024.xlsx",
                       sheet_name="Table 5",
                       # engine="openpyxl",
                       skiprows=1
                       )
    st.dataframe(df)

elif selected == 4.2:
    df = pd.read_excel("assets/579 RCS Routes Operationalised as on 08.07.2024.xlsx",
                       sheet_name="Table 6",
                       # engine="openpyxl",
                       skiprows=1
                       )
    st.dataframe(df)

elif selected == 4.3:
    df = pd.read_excel("assets/579 RCS Routes Operationalised as on 08.07.2024.xlsx",
                       sheet_name="Table 7",
                       # engine="openpyxl",
                       skiprows=1
                       )
    st.dataframe(df)

elif selected == 5.0:
    df = pd.read_excel("assets/579 RCS Routes Operationalised as on 08.07.2024.xlsx",
                       sheet_name="Table 8",
                       # engine="openpyxl"
                       )
    st.dataframe(df)

elif selected == 5.1:
    df = pd.read_excel("assets/579 RCS Routes Operationalised as on 08.07.2024.xlsx",
                       sheet_name="Table 9",
                       # engine="openpyxl",
                       skiprows=1,
                       skipfooter=1
                       )
    st.dataframe(df)

elif selected == 5.3:
    df = pd.read_excel("assets/579 RCS Routes Operationalised as on 08.07.2024.xlsx",
                       sheet_name="Table 10",
                       # engine="openpyxl",
                       skiprows=1,
                       nrows=8

                       )
    st.dataframe(df)
