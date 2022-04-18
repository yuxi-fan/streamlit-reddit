from datetime import datetime
import streamlit as st
from google.cloud import firestore
import numpy as np
import pandas as pd
import plotly.express as px


def app():
    
    st.title("Covid Trend")