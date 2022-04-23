from datetime import datetime
import streamlit as st
from google.cloud import firestore
import numpy as np
import pandas as pd
import plotly.express as px


def app():
    
    st.title("City Unemployment Trend")
    db = firestore.Client.from_service_account_json("firestore_key.json")
    posts_ref = db.collection("city_weekly")

    df = pd.DataFrame(columns=('datetime', 'cityname','nitclaims_rate_regular'))
    for doc in posts_ref.stream():
        ui = doc.to_dict()
        try:
            date_time = ui['datetime']
            city_name = ui['cityname']
            uirate = ui['initclaimsRateRegular']
            df.loc[len(df)] =[date_time, city_name, uirate]
        except:
            continue

    df = df.sort_values('datetime')
    #st.dataframe(df)

    unique_city = ['San Jose','Los Angeles','Chicago','Washington','New York City','Seattle','San Francisco']
    select_city = st.sidebar.selectbox('City',unique_city)
    input_city = select_city
    selected_df = df.loc[df['cityname']==input_city]
    selected_df = selected_df.sort_values('datetime')
    selected_df['nitclaims_rate_regular'] = selected_df['nitclaims_rate_regular'].apply(pd.to_numeric)
    title_str = 'UI claims for ' + select_city
    fig = px.line(selected_df, x="datetime", y="nitclaims_rate_regular", title=title_str)
    st.plotly_chart(fig)

    select_citys = st.sidebar.multiselect('Select city for comparison',unique_city)
    compare_df = df[df.cityname.isin(select_citys)]
    idx = compare_df.groupby('cityname')['datetime'].transform(max) == compare_df['datetime']
    max_date_df = compare_df[idx]
    #compare_df = df.loc[df[datetime] == ]
    max_date_df['nitclaims_rate_regular'] = max_date_df['nitclaims_rate_regular'].apply(pd.to_numeric)
    fig = px.bar(max_date_df,x = 'cityname',y = 'nitclaims_rate_regular')
    if st.button("Show comparison"):
        st.plotly_chart(fig)
  
    """ if st.button('San Jose'):
        input_city = 'San Jose'
        selected_df = df.loc[df['cityname']==input_city]
        selected_df = selected_df.sort_values('datetime')
        selected_df['nitclaims_rate_regular'] = selected_df['nitclaims_rate_regular'].apply(pd.to_numeric)
        fig = px.line(selected_df, x="datetime", y="nitclaims_rate_regular", title='UI claims for selected city')
        st.plotly_chart(fig)
  
    if st.button('Chicago'):
        input_city = 'Chicago'
        selected_df = df.loc[df['cityname']==input_city]
        selected_df = selected_df.sort_values('datetime')
        selected_df['nitclaims_rate_regular'] = selected_df['nitclaims_rate_regular'].apply(pd.to_numeric)
        fig = px.line(selected_df, x="datetime", y="nitclaims_rate_regular", title='UI claims for selected city')
        st.plotly_chart(fig)
  
    if st.button('Los Angeles'):
        input_city = 'Los Angeles'
        selected_df = df.loc[df['cityname']==input_city]
        selected_df = selected_df.sort_values('datetime')
        selected_df['nitclaims_rate_regular'] = selected_df['nitclaims_rate_regular'].apply(pd.to_numeric)
        fig = px.line(selected_df, x="datetime", y="nitclaims_rate_regular", title='UI claims for selected city')
        st.plotly_chart(fig)

    if st.button('Washington'):
        input_city = 'Washington'
        selected_df = df.loc[df['cityname']==input_city]
        selected_df = selected_df.sort_values('datetime')
        selected_df['nitclaims_rate_regular'] = selected_df['nitclaims_rate_regular'].apply(pd.to_numeric)
        fig = px.line(selected_df, x="datetime", y="nitclaims_rate_regular", title='UI claims for selected city')
        st.plotly_chart(fig)


    if st.button('Seattle'):
        input_city = 'Seattle'
        selected_df = df.loc[df['cityname']==input_city]
        selected_df = selected_df.sort_values('datetime')
        selected_df['nitclaims_rate_regular'] = selected_df['nitclaims_rate_regular'].apply(pd.to_numeric)
        fig = px.line(selected_df, x="datetime", y="nitclaims_rate_regular", title='UI claims for selected city')
        st.plotly_chart(fig)


    if st.button('San Francisco'):
        input_city = 'San Francisco'
        selected_df = df.loc[df['cityname']==input_city]
        selected_df = selected_df.sort_values('datetime')
        selected_df['nitclaims_rate_regular'] = selected_df['nitclaims_rate_regular'].apply(pd.to_numeric)
        fig = px.line(selected_df, x="datetime", y="nitclaims_rate_regular", title='UI claims for selected city')
        st.plotly_chart(fig)


    if st.button('New York City'):
        input_city = 'New York City'
        selected_df = df.loc[df['cityname']==input_city]
        selected_df = selected_df.sort_values('datetime')
        selected_df['nitclaims_rate_regular'] = selected_df['nitclaims_rate_regular'].apply(pd.to_numeric)
        fig = px.line(selected_df, x="datetime", y="nitclaims_rate_regular", title='UI claims for selected city')
        st.plotly_chart(fig)

 """