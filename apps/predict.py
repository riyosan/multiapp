import streamlit as st
...
from apps.preprocess import *

def upload_dataset_pred():
  with st.header("1. Upload your CSV data"):
    data_pred=st.file_uploader("Upload File CSV",type=['csv'])
    return data_pred
def prepro_pred(pred):
  return predicted
def app():
  global data_pred
  dataset = upload_dataset_pred()
  if dataset is not None:
    pred = pd.read_csv(dataset)
    if st.button("predict Data"):
      st.write(pred)
      prepro_pred(pred)
  else:
    if st.button('Press to use Example Dataset'):
      pred = pd.read_csv('testing.csv')
      prepro_pred(pred)
