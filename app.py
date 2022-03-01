import streamlit as st
from PIL import Image
from multiapp import MultiApp
from apps import praproses, data, prediksi # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Preprocess", praproses.app)
app.add_app("Train & Test", train_test.app)
app.add_app("Predict", predict.app)
# The main app
app.run()
