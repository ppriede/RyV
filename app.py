from multiapp import MultiApp
from apps import home, data_stats, divergencia_geometrica_v1  # import your app modules here
import streamlit as st

app = MultiApp()

# Add all your application here
app.add_app("Divergencia geométrica simple", divergencia_geometrica_v1.app)
app.add_app("Home", home.app)
app.add_app("Data Stats", data_stats.app)

# The main app
app.run()