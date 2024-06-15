import streamlit as st

st.title("All About KYLE ESCARILLA 🙎🏻‍♂️")



st.title("📷: Imahe")


image_paths = ["./pic/kyle.jfif"]


cols = st.columns(len(image_paths))

for col, image_path in zip(cols, image_paths):
    col.image(image_path)


st.header("👨‍🎓 ESCARILLA, KYLE BRIAN LACSON")



# Personal Information
st.header("Personal Information")
st.write("**Name:** KYLE BRIAN LACSON ESCARILLA")
st.write("**Age:** 21 years old")
st.write("**Education:** Currently studying at CARLOS HILADO MEMORIAL STATE UNIVERSITY")
st.write("**Year:** 3rd year Bachelor of Science in Information Systems Student")
st.write("**Location:** Silay City Negros Occidental")

st.header("My Hobby")
st.image("pic/ball.jpg")
st.markdown("""* Playing basketball involves dribbling, shooting, and passing, which improves coordination, balance, and cardiovascular health. It also fosters teamwork and communication skills, as players work together to achieve common goals.
* Music can evoke emotions, stimulate memories, and inspire creativity. Whether enjoying favorite genres, exploring new artists, or attending live concerts, listening to music fosters a deep connection to one's personal identity and cultural heritage. 
* Partying is a lively and social hobby that involves gathering with friends or groups to celebrate, dance, and enjoy music. It provides an opportunity to relax, have fun, and create memorable experiences in a festive atmosphere.
            """, unsafe_allow_html=True)

st.header("🎧ྀིMusic Genre")

st.write("**▶︎ •၊၊||၊|။||||| 0:19")
st.write("**🎸:** listening to Rock music can change the mood.")
st.write("**🤘🏻 :** Reggae Music a good music also.")




st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        padding: 2em;
    }
    h1, h2 {
        color: RED;
    }
    .stText {
        font-size: 1.2em;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Footer or additional sections (optional)
st.write("### Thank you for visiting my profile!")

