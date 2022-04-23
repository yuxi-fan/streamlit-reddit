from datetime import datetime
import streamlit as st
from google.cloud import firestore
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components

def app():
    st.title("Comparison of Unemployment Rate in China and the US")
    genre = st.radio(
     "Please select a year below",
     ('2017','2018','2019','2020','2021'))
  
    if genre == '2017':
        HtmlFile = open("frontend/2017.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        print(source_code)
        components.html(source_code,width=1500,height=900)
    
    if genre == '2018':
        HtmlFile = open("frontend/2018.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        print(source_code)
        components.html(source_code,width=1500,height=900)

    if genre == '2019':
        HtmlFile = open("frontend/2019.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        print(source_code)
        components.html(source_code,width=1500,height=900)
    
    if genre == '2020':
        HtmlFile = open("frontend/2020.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        print(source_code)
        components.html(source_code,width=1500,height=900)

    if genre == '2021':
        HtmlFile = open("frontend/2021.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        print(source_code)
        components.html(source_code,width=1500,height=900)