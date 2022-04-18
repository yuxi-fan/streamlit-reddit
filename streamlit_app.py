import streamlit as st
from google.cloud import firestore
import numpy as np
import pandas as pd

from multipage import MultiPage
from apps import uiclaims, covid# import your pages here



# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("Employment Checker")
st.header("A website you can used to check employment status in the United State")
st.subheader("build by Chaoyu Li, Joanna Xiao, Yuxi Fan")
# Add all your applications (pages) here
app.add_page("UI Claims", uiclaims.app)
app.add_page("COVID Trend", covid.app)
# The main app
app.run()


#db = firestore.Client.from_service_account_json("firestore_key.json")
#posts_ref = db.collection("UIclaims")

#for doc in posts_ref.stream():
#	ui = doc.to_dict()
#	title = ui["year"]
#	url = ui["month"]

#	st.subheader(f"Year: {title}")
#	st.write(f":Month: [{url}]({url})")
