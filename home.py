
import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()
show_pages(
    [   
        Page("home.py", "ITEQMT Machine Learning Application Portfolio", "👾"),
        Section("Main Page", "⭐"),
        Page("pages/aboutme.py", "🙎🏻‍♂️All About Kyle", "1️⃣", in_section=True),
        Page("pages/description.py", "📝Project Descriptions", "2️⃣", in_section=True),
        Page("pages/learnings.py", "🔎 ITEQMT Insights", "3️⃣", in_section=True),
     
  
        Section("Sample Projects", "🗂️"),
        Page("pages/analyzer.py", "📋Feelings Analyzer", "1️⃣", in_section=True),
        Page("pages/classification.py", "🍆Vegetables Classification", "2️⃣", in_section=True),
        Page("pages/prediction.py", "🔮 Prediction", "3️⃣", in_section=True),

        Section("Project Source Code","💻"),
        Page("pages/analyze_src.py","Sentiment Analyzer SRC", "1️⃣", in_section=True),
        Page("pages/classification_src.py","Image Classificatiom SRC", "2️⃣", in_section=True),
        Page("pages/prediction_src.py","Prediction SRC", "3️⃣", in_section=True),
        
    ]
)

hide_pages(["Thank you"])

st.markdown("### FINAL PROJECT REQUIREMENTS: ")
st.header("ESCARILLA, KYLE BRIAN of BSIS 3B")
st.image("./pic/st1.png")
st.markdown("""<a href="/photographer/thinkstock-83786">Thinkstock</a> on <a href="/">Freeimages.com</a>""",unsafe_allow_html=True,)


st.info("👨‍🔧 Please take note when on streamlit.app the [Image Classification] pages are not working due to Memory Limitation of 'Free Tier' hosting of Streamlit") 
st.markdown("---")

with st.expander("What is STREAMLIT?"""):
    st.markdown("""
    
    
    #

                Streamlit
 is an open-source Python library designed for creating and sharing custom web applications for machine learning and data 
                science projects. It simplifies the process of transforming data scripts into interactive web apps without 
                requiring extensive web development knowledge.

                 USAGE
Streamlit allows developers and data scientists to build web applications by writing straightforward Python code. 
                To create an app, users need to install Streamlit via pip, write a Python script utilizing Streamlit's
                 API to define the app's layout and interactivity, and then run the script. The framework supports various widgets like sliders,
                 buttons, and graphs, making it easy to create dynamic user interfaces that respond to user input.
                
                 BENEFITS
* Ease of Use: Streamlit's simplicity and intuitive API allow developers to quickly prototype and deploy applications without worrying about the complexities of front-end development.
* Interactive Visualizations: It supports a wide range of interactive widgets and can integrate seamlessly with popular data visualization libraries like Matplotlib, Plotly, and Altair.
* Real-time Data Display: Streamlit enables real-time updates and interactions, making it ideal for dashboards and live data monitoring.
* Collaboration and Sharing: Applications can be easily shared with others, enabling collaboration and feedback from stakeholders.
* Open Source and Community Support: Being open-source, Streamlit has a growing community that contributes to its development and provides extensive resources and support for users.

    #""", unsafe_allow_html=True)

st.title('QUANTITATIVE METHODS')

st.markdown("""


##### 👨‍🔧 KEY FEATURES OF QUANTITATIVE METHODS

* Numerical Data: Quantitative research focuses on gathering numerical data that can be quantified and subjected to statistical analysis.
* Objectivity: Emphasizes objectivity and aims to produce findings that are replicable and generalizable.
* Structured Approach: Involves structured research instruments such as surveys, questionnaires, and standardized tests to collect data.
* Statistical Analysis: Utilizes statistical techniques to analyze data, identify patterns, relationships, and test hypotheses.
### 🔎 Overview""", unsafe_allow_html=True)


st.image("./pic/st2.webp")

st.header("Common Techniques in Quantitative Methods")
st.markdown(""" * Surveys and Questionnaires: Tools for collecting large amounts of data from a sample population to understand attitudes, behaviors, or characteristics.
* Experiments: Controlled studies designed to test specific hypotheses by manipulating variables and observing the effects on other variables.
* Correlational Studies: Research that explores the relationship between two or more variables to determine if they are associated.
* Longitudinal Studies: Studies that follow the same subjects over a period of time to observe changes and developments.  """,unsafe_allow_html=True,)

st.header("Benefits of Quantitative Methods")
st.markdown(""" * Precision and Accuracy: Provides precise measurements and quantitative data that can be statistically validated.
* Generalizability: Results from a representative sample can often be generalized to a larger population.
* Replicability: Structured methods and statistical analysis allow for replication of studies, ensuring reliability of findings.
* Predictive Power: Can be used to make predictions about future trends and behaviors based on existing data.  """,unsafe_allow_html=True,)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
