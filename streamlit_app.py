import streamlit as st
from google.cloud import firestore
import numpy as np
import pandas as pd



from multipage import MultiPage
from apps import uiclaims, covid, cityweekly# import your pages here



# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.image('title1.png', use_column_width = True)

st.header("A website you can use to check employment status in the United States")
st.subheader("build by Chaoyu Li, Joanna Xiao, Yuxi Fan")


# Add all your applications (pages) here
app.add_page("UI Claims", uiclaims.app)
app.add_page("COVID Trend", covid.app)
app.add_page("City Weekly", cityweekly.app)
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
