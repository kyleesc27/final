import streamlit as st

st.title("Description of Different Streamlit Application")


st.header('Simple Sentiment Analyzer App')
st.image("./pic/analyze.jfif")

with st.expander("🔮Sentiment Analyzer"):
    st.markdown("""
    
    #
                A Sentiment Analyzer 
Sentiment analysis is like a smart tool that reads text to figure out if it's happy, sad, or just okay. It uses special computer tricks and learning from lots of examples to do this. It looks at things like the words used, how they're put together, and what they mean in the text. For example, if you write "I love this game!", it knows you're happy because of the word "love" and the excitement. But if you say "I hate waiting in line," it understands you're not happy. People use this tool a lot to understand what others feel when they write things online or in reviews.

                
    """, unsafe_allow_html=True)

st.header('👨‍🌾Image Classification')
st.image("./pic/class.png")

with st.expander("Image Classification Project"):
    st.markdown("""
    
    #
                Image Classification
    In my vegetable classification project, the main aim is to accurately identify various types of vegetables from images that users upload. The project specifically focuses on sorting images into different categories based on the type of vegetable they depict.
                
    """, unsafe_allow_html=True)

st.header('🔍Prediction')
st.image("./pic/pre1.jfif")

with st.expander("Prediction"):
    st.markdown("""
    
    #
               Data Prediction
Data predictions on datasets from Kaggle involve using statistical or machine learning models to forecast outcomes based on the provided data. Kaggle is a platform that hosts datasets and machine learning competitions, where participants develop predictive models to solve specific problems.

Participants typically download datasets from Kaggle, which contain features (variables) and target variables (what they want to predict). They then preprocess the data, which involves cleaning, transforming, and preparing it for modeling. Next, they select appropriate predictive models, such as regression, classification, or clustering algorithms, based on the nature of the prediction task.

                
    """, unsafe_allow_html=True)