from datetime import datetime
import streamlit as st
from google.cloud import firestore
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components

def app():
    option = st.selectbox(
     'Choose the visualization',
     ('COVID vs Unemployment Claims','Employment level of different size company', 'Employment level of different industry',"Unemployment Claims",'COVID vs Employment Level'))

    if option == 'Employment level of different size company':
        st.title("Employment level of different size company")
        HtmlFile = open("frontend/employment_company.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        print(source_code)
        components.html(source_code,width = 1200,height = 900)

    if option == 'Employment level of different industry':
        st.title("Employment level of different industry")
        HtmlFile = open("frontend/employment_industry.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        print(source_code)
        components.html(source_code,width = 1200,height = 900)

    if option == "Unemployment Claims":
        st.title("Unemployment Claims")
        HtmlFile = open("frontend/ui.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        print(source_code)
        components.html(source_code,width = 1400,height = 900)

    if option == 'COVID vs Unemployment Claims':
        st.title('COVID vs Unemployment Claims')
        HtmlFile = open('frontend/dy_UI.html', 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        print(source_code)
        components.html(source_code,width = 1400,height = 900)

    if option == 'COVID vs Employment Level':
        st.title('COVID vs Employment Level')
        HtmlFile = open('frontend/dy.html', 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        print(source_code)
        components.html(source_code,width = 1400,height = 900)