import streamlit as st
from multiapp import MultiApp
from apps import home, data, model, finance # import your app modules here

app = MultiApp()

st.markdown("""
# Multi-Page App

This is muli-page app where you can select an app from multiple apps

""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Data", data.app)
app.add_app("Model", model.app)
app.add_app("finance", finance.app)
# The main app
app.run()
