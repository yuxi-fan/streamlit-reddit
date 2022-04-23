from datetime import datetime
import streamlit as st
from google.cloud import firestore
import numpy as np
import pandas as pd
import plotly.express as px

def app():

    st.subheader("Prediction model visualization")
    st.image('pics/model.png', use_column_width = True)

    st.subheader("Interactive graph")
    db = firestore.Client.from_service_account_json("firestore_key.json")
    posts_ref = db.collection("prediction")

    df = pd.DataFrame(columns=('datetime', 'rate'))
    for doc in posts_ref.stream():
        ui = doc.to_dict()
        try:
            date_time = ui['date']
            emp = ui['emp']
            df.loc[len(df)] =[date_time, emp]
        except:
            continue

    df = df.sort_values('datetime')
    #st.dataframe(df)

    df['rate'] = df['rate'].apply(pd.to_numeric)

    fig = px.line(df, x="datetime", y="rate", title="Interactive graph")
    st.plotly_chart(fig)