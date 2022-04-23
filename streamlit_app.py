import streamlit as st
from google.cloud import firestore
import numpy as np
import pandas as pd



from multipage import MultiPage
from apps import main, visualization, cityweekly, model, water, heatmap# import your pages here



# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.image('pics/title.png', use_column_width = True)

st.header("A website you can use to check employment status in the United States")
st.write("build by Chaoyu Li, Joanna Xiao, Yuxi Fan")


# Add all your applications (pages) here
app.add_page("Home Page", main.app)
app.add_page("Visualizations", visualization.app)
app.add_page("Unemployment rate for major cities", cityweekly.app)
app.add_page("Prediction Model", model.app)
app.add_page("US Heatmap", heatmap.app)
app.add_page("China and the US comparison", water.app)
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
