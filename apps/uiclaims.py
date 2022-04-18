from datetime import datetime
import streamlit as st
from google.cloud import firestore
import numpy as np
import pandas as pd
import plotly.express as px


def app():
    
    st.title("UI Claims trend")
    db = firestore.Client.from_service_account_json("firestore_key.json")
    posts_ref = db.collection("UIclaims")

    df = pd.DataFrame(columns=('Year', 'Month', 'date', 'New unemployment claim count'))
    for doc in posts_ref.stream():
        ui = doc.to_dict()
        year = ui["year"]
        month = ui["month"]
        date = ui["dayEndofweek"]
        count_ = ui["initclaimsCountCombined"]
        df.loc[len(df)] =[year, month, date,count_]

    df["datetime"]=pd.to_datetime(df.Year+df.Month+df.date,format="%Y%m%d")
    df['New unemployment claim count'] = df['New unemployment claim count'].apply(pd.to_numeric)
    df = df.sort_values('datetime')
    st.dataframe(df)
    fig = px.line(df, x="datetime", y="New unemployment claim count", title='New unemployment claim count')
    st.plotly_chart(fig)