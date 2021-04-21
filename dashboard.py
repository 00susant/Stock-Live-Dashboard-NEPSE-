import streamlit as st
import plotly.express as px
import pandas as pd
import pymongo


@st.cache
def load_data():
	# Connecting MongoDb
	# Establishing connection with the mongodb
	mongodb_client = pymongo.MongoClient("mongodb+srv://susant:susant@cluster0.yevtz.mongodb.net/Merolagani?retryWrites=true&w=majority")

	merolaganiDb = mongodb_client.Merolagani
	collection = merolaganiDb.test


	df = pd.DataFrame(list(collection.find()))
	#print(df.head())

	#def load_data():
	numeric_df = df.select_dtypes(['float', 'int'])
	numeric_cols = numeric_df.columns
	text_df = df.select_dtypes(['object'])
	text_cols = text_df.columns
	companies = df['Symbol'].unique()
	return df, numeric_cols, text_cols, companies


df, numeric_cols, text_cols, companies = load_data()



# Showing the title of dashboard
st.title(
    "Nepse DashBoard"
)

# checkbox options for dataset
check_box = st.sidebar.checkbox(label = 'Show Dataset')


# Stating condition	
if check_box:
	# Showing dataframe
	st.write(df)

# Title of sidebar
st.sidebar.title('Settings')

st.sidebar.subheader("Time Series")

feature_selection = st.sidebar.multiselect(label = 'Features to Plot', options = numeric_cols)
stock_dropdown = st.sidebar.selectbox(label = 'Companies', options = companies)


df = df.set_index('DateTime')
df = df[df['Symbol'] == stock_dropdown]
df_features = df[feature_selection]
print(df_features)

plotly_figure = px.line(data_frame = df_features, x = df_features.index, y = feature_selection,  width=800, height=500)

plotly_figure.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="LightSteelBlue",
)
st.plotly_chart(plotly_figure)
