import streamlit as st
import joblib
from sklearn import svm


filename = 'classifier.sav'
classifier_linear=joblib.load(open(filename,'rb'))
filename1 = 'vectorizer.sav'
vectorizer=joblib.load(open(filename1,'rb'))

st.title('Sentiment Analysis using Machine Learning Algorithms')
text=st.text_area('Enter text')

st.set_option('deprecation.showfileUploaderEncoding', False)

if st.button("Predict"):
  review_vector = vectorizer.transform([text])
  x=classifier_linear.predict(review_vector)
  if (x[0]=='0'):
    st.success('Text is  NEUTRAL')
  if (x[0]=='1'):
    st.success('Text is POSITIVE')
  if (x[0]=='-1'):
    st.success(' Text is NEGATIVE')
