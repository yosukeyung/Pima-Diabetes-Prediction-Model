import streamlit as st
import joblib as jb
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title='Prediction Diabetes',page_icon='🩺')
st.title('Prediction Diabetes')
st.caption('made by yosuke')

def load_model():
  return jb.load('logreg.pkl')

model=load_model()

st.subheader('Enter Features')
col1,col2,col3,col4,col5,col6,col7,col8=st.columns(8)

with col1:
  r1=st.number_input('Pregnancies',value=0.0,format='%.4f')

with col2:
  r2=st.number_input('Glucose',value=0.0,format='%.4f')

with col3:
  r3=st.number_input('Blood Pressure',value=0.0,format='%.4f')

with col4:
  r4=st.number_input('Skin Thickness',value=0.0,format='%.4f')

with col5:
  r5=st.number_input('Insulin',value=0.0,format='%.4f')

with col6:
  r6=st.number_input('BMI',value=0.0,format='%.4f')

with col7:
  r7=st.number_input('Diabetes Pedigree Function',value=0.0,format='%.4f')

with col8:
  r8=st.number_input('Age',value=0.0,format='%.4f')

if st.button('Predict'):
  x=np.array([[r1,r2,r3,r4,r5,r6,r7,r8]])
  prob_diab=model.predict_proba(x)[0][1]
  pred='Diabetic' if prob_diab>=0.5 else 'Not Diabetic'
  st.success(f'Prediction : **{pred}**\nProbability : **{prob_diab}**')

  fig,ax=plt.subplots()
  ax.bar(['Diabetic','Not Diabetic'],[prob_diab,1-prob_diab])
  ax.set_ylim(0,1)
  ax.set_ylabel('Prediction')
  st.pyplot(fig)