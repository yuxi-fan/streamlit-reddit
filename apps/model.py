from datetime import datetime
import streamlit as st
from google.cloud import firestore
import numpy as np
import pandas as pd
import plotly.express as px
import requests
import json

def app():

    st.subheader("Prediction model visualization")
    st.image('pics/model.png', use_column_width = True)

    st.subheader("Interactive graph")
    baseURL = 'https://dsci551-project-c5c44-default-rtdb.firebaseio.com/'
    def query_data(path):
        getURL = baseURL + '/' + path + '.json'
        response = requests.get(getURL)
        return json.loads(response.text)
    jsonData = query_data("US-Employment-National-Predict")
    #jsonData = query_data("US-COVID19-National")
    df = pd.DataFrame(jsonData).transpose()
    rowname = df.index
    col_name=df.columns.tolist()
    col_name.insert(0,'date')
    df_new=df.reindex(columns=col_name)
    df_new['date']=rowname
    df_new.date = pd.to_datetime(df_new.date)
    df_new = df_new.sort_values(by='date',ascending=True)

    fig = px.line(df_new, x="date", y="emp", title='Change of employment level prediction')
    st.plotly_chart(fig)