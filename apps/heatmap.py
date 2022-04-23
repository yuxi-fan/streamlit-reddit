from datetime import datetime
import streamlit as st
from google.cloud import firestore
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components

def app():
    st.title("Latest unemployment rate in the United State")
    HtmlFile = open("frontend/heatmap_emp.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code,width=1500,height=900)