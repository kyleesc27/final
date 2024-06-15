import streamlit as st
st.set_page_config(layout="wide", page_title="Learnings")

st.title("🧑🏻‍🎓What I have Learned")
st.header('🏆Learnings..!')

st.image("./pic/learn.jpg")

st.markdown("""
#
                Studying Quantitative Methods:
    It equipped me with a comprehensive understanding of the essential skills and techniques
    needed to analyze and interpret data.This course has provided me with the expertise required
    for various applications, from basic data analysis to more complex tasks such as image 
    classification and sentiment analysis. The knowledge and skills acquired from this 
    subject will undoubtedly serve as a cornerstone for my future goals.
 
    The subject of Quantitative Methods has been a transformative educational experience, providing 
    me with vital skills and knowledge essential for my future pursuits. From basic coding and data 
    analysis to advanced applications like image classification and sentiment analysis, the capabilities
    gained from this course will empower me to make meaningful contributions in my chosen field and beyond.           
            """, unsafe_allow_html=True)

with st.expander("🔧Benefits of Studying this Subject"):
    st.markdown("""
    
    #
                Studying Image Classification
It offers numerous benefits, as it equips individuals with practical skills applicable across various domains. 
Through understanding data preprocessing, machine learning model training, and performance evaluation, one can develop 
systems proficient in accurately categorizing images. 
                
                Sentiment Analysis:
Similarly, delving into Sentiment Analysis provides tangible advantages by enabling individuals to analyze textual data
                and extract sentiment—whether positive, negative, or neutral. Building sentiment analyzers proves invaluable in 
                areas like market research, customer feedback analysis, and social media monitoring. By amalgamating data analysis 
                techniques with natural language processing (NLP), individuals can develop tools facilitating businesses in comprehending 
                customer sentiments and refining their products and services accordingly. 

                Data Prediction:
Data predictions offer numerous benefits, including improved decision-making, risk mitigation, resource optimization, and enhanced 
competitiveness. However, it's essential to validate predictive models, monitor their performance, and update them regularly to ensure 
accuracy and relevance in dynamic environments.
                

    """, unsafe_allow_html=True)