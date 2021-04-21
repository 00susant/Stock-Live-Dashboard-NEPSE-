import streamlit as st
import plotly.express as px
import pandas as pd
import pymongo


def load_data()
	# Connecting MongoDb
	# Establishing connection with the mongodb
	mongodb_client = pymongo.MongoClient("mongodb+srv://susant:susant@cluster0.yevtz.mongodb.net/Merolagani?retryWrites=true&w=majority")

	merolaganiDb = mongodb_client.Merolagani
	collection = merolaganiDb.test


	df = pd.DataFrame(list(collection.find()))
	print(df.head())

	#def load_data():
	numeric_df = df.select_dtypes(['float', 'int'])
	numeric_cols = numeric_df.columns
	text_df = df.select_dtypes(['object'])
	text_cols = text_df.columns
	return df, numeric_cols, text_cols


df, numeric_cols, text_cols = load_data()


'''
# Showing the title of dashboard
st.title(
    "Nepse DashBoard"
)

# Showing dataframe
st.write(df)
'''