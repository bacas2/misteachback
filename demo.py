import streamlit as st
import pandas as pd
import plotly.express as px


st.header('Cars data', divider='blue')

@st.cache_data
def get_data():
    return pd.read_csv('https://drive.google.com/uc?id=1OAIj0iDC7nIUOvt8ZejNLdvPvbg-MOUw&export=download')

df = get_data()
st.dataframe(df)

manufacturers = sorted(df['manufacturer'].unique())
manu_choice = st.selectbox('Manufacturer filter', manufacturers)
manu_df = df.loc[df['manufacturer'] == manu_choice]

st.header(f'Number of {manu_choice} cars for sale by model year', divider='blue')
fig = px.histogram(manu_df, x="year")
st.plotly_chart(fig)
