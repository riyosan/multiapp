import streamlit as st
...
@st.experimental_memo
def load_dataset():
  df = pd.read_csv('fintech_data.csv')
  return df

@st.experimental_memo
def preprocessing():
  df=load_dataset()
  ...
  return df

@st.experimental_memo
def funneling():
  ...
  return df_numerik

def app():
  dataset = st.sidebar.file_uploader("Upload Your File CSV", type=['csv'])
  if dataset is not None:
    df = load_dataset(dataset)
    st.dataframe(df)
  else:
    #initialize session state
    if "load_state" not in st.session_state:
      st.session_state.load_state = False
    if st.button('load data') or st.session_state.load_state:
      st.session_state.load_state = True
      df=pd.read_csv('fintech_data.csv')
      st.dataframe(df)
      st.write(load_dataset())
      df=preprocessing()
      df_numerik=funneling()
      st.write(df_numerik)