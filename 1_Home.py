import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(
    page_title="Cutis",
    page_icon=":heart:",
    layout="centered",
    initial_sidebar_state="collapsed"
)

def set_background(image_file):
    """
    This function sets the background of a Streamlit app to an image specified by the given image file.

    Parameters:
        image_file (str): The path to the image file to be used as the background.

    Returns:
        None
    """
    with open(image_file, "rb") as f:
        img_data = f.read()
    b64_encoded = base64.b64encode(img_data).decode()
    style = f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{b64_encoded});
            background-size: cover;
        }}
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)

set_background('bg_image.png')

st.sidebar.title("Menu")

st.title("Home")
st.divider()

st.write("Welcome!")


# st.link_button("Get started by clicking here!", https://cutis-ai.streamlit.app/Profile)
# st.link_button("Comfort and confidence :heart:", https://cutis-ai.streamlit.app/Quotes)
# st.link_button("Learn more about happy healthy lifestyles!", https://cutis-ai.streamlit.app/Info_Hub)

# ALTERNATIVE METHOD
# st.markdown("<a href='#4_Profile'>Get started by clicking here!</a>", unsafe_allow_html=True)
# st.markdown("<a href='#2_Quotes'>Comfort and confidence</a>", unsafe_allow_html=True)
# st.markdown("<a href='#3_Info_Hub'>Learn more about happy healthy lifestyles!</a>", unsafe_allow_html=True)

# DATA RETRIEVAL
# import pandas as pd 
# data = pd.read_csv("data.csv")
# st.write(data)