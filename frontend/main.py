import streamlit as st
from streamlit_option_menu import option_menu
import requests
# from ..backend.app import predict_sentiment_all_emiten

def process_one(news : str):

    r = requests.post(f"http://127.0.0.1:8000/predict_sentiment_all_emiten/?news={news}")
    
    return r

def process_two(news : str, aspect : str):

    t = requests.post(f"http://127.0.0.1:8000/predict_sentiment_specific_emiten/?news={news}&aspect={aspect}")
    
    return t

# UI Layout

with st.sidebar:
    choose = option_menu("Predict", ["All Emiten", "Specific Emiten"],
                         icons=['grid fill', 'search heart'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "20px"}, 
        "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

if choose == "All Emiten":
    st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Sentiment Analysis</p>', unsafe_allow_html=True)    
    st.subheader("Sentiment Analysis of Indonesian Stock Company Articles with BERT.")

    st.caption("Predict Sentiment All Emiten")
    with st.form(key='nlpForm'):
        news = st.text_area("Enter Article Here", height:200)
        submit_button = st.form_submit_button(label='Analyze')
        
        if submit_button:
            st.info("Results")
            predict = process_one(news)
            st.write(predict)
            st.json(predict.text)

elif choose == "Specific Emiten":
    st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Sentiment Analysis</p>', unsafe_allow_html=True)    
    st.subheader("Sentiment Analysis of Indonesian Stock Company Articles with BERT.")
    
    st.caption("Predict Sentiment Specific Emiten")
    with st.form(key='nlpForm'):
        news = st.text_area("Enter Article Here", height:200)
        aspect = st.text_input("Enter Aspect Here")
        submit_button = st.form_submit_button(label='Analyze')
        
        if submit_button:
            st.info("Results")
            predict = process_two(news, aspect)
            st.write(predict)
            st.json(predict.text)        
