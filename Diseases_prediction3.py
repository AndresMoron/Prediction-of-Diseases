


import pickle
import streamlit as st
from streamlit_option_menu import option_menu



heart_disease_model = pickle.load(open('C:/Users/andre/Desktop/Disease_prediction/Models/heart3.py', 'rb'))



# Sidebar for navigate

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          [
                           'Heart Disease Prediction'],
                          
                          default_index=0)
    

    
#heart prediction page
if(selected == 'Heart Disease Prediction'):
    st.title('Predicción de problemas del corazón con uso de ML')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #cancer_model = pickle.load(open('C:/Users/andre/Desktop/Disease_prediction/Models/cancer3.py', 'rb'))
    
#parkinson_model = pickle.load(open("C:/Users/andre/Desktop/Models/parkinson.py"))