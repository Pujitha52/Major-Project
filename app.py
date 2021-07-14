import streamlit as st
import joblib
model = joblib.load('Sentiment-Analysis')
st.title('Sentiment Analysis using Machine Learning Algorithms')
ip = st.text_input('Enter your message')
op = model.predict([ip])
if st.button('Predict'):
  if (op[0]=='0'):
    st.success('Text is  NEUTRAL')
  if (op[0]=='1'):
    st.success('Text is POSITIVE')
  if (op[0]=='-1'):
    st.success(' Text is NEGATIVE')
