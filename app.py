import streamlit as st
st.set_page_config(page_title='Skripsi', layout='wide')
from PIL import Image
from multiapp import MultiApp
from apps import praproses, data, prediksi # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Preprocess", praproses.app)
app.add_app("Train & Test", data.app)
app.add_app("Predict", prediksi.app)
# The main app
app.run()
