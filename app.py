import streamlit as st
import pandas as pd
import plotly.express as px

####################################################
# import the data
####################################################
@st.cache_data
def get_data() -> pd.DataFrame:
    return pd.read_csv('https://drive.google.com/uc?id=1OAIj0iDC7nIUOvt8ZejNLdvPvbg-MOUw&export=download')

df = get_data()

st.header('This is all of the data', divider='blue')
st.dataframe(df)

df['year_ts'] = pd.to_datetime(df['year'], format="%Y")


####################################################
# histogram with manufacturer filter
####################################################

manu_choice = st.sidebar.selectbox('Manufacturer filter', sorted(df['manufacturer'].unique()))
manu_df = df.loc[df['manufacturer'] == manu_choice]



fig = px.histogram(manu_df, x="year_ts")
st.header(f"Number of {manu_choice} vehicles from a given year")
st.plotly_chart(fig)

####################################################
# Average price of vehicles over time
####################################################

condition_choice = st.sidebar.selectbox('Quality filter', sorted(df['car_condition'].unique()))

manu_df['avg_price'] = manu_df.groupby(manu_df.year)['price'].transform('mean')

manu_quality_df = manu_df.loc[df['car_condition'] == condition_choice]

st.header(f"Average price of {condition_choice} {manu_choice} vehicles")
st.line_chart(manu_quality_df, x="year_ts", y="avg_price")
