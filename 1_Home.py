import streamlit as st

st.set_page_config(
    page_title="Acneeds",
    page_icon=":heart:",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.sidebar.title("Menu")

st.title("Home")
st.divider()

st.write("Welcome!")

# ONCE DEPLOYED INSERT LINKS AND UNCOMMENT THIS
# st.link_button("Get started by clicking here!", LINK_TO_4_PROFILE.PY)
# st.link_button("Comfort and confidence :heart:", LINK_TO_2_QUOTES.PY)
# st.link_button("Learn more about happy healthy lifestyles!", LINK_TO_3_INFO_HUB.PY)

# ALTERNATIVE METHOD
# st.markdown("<a href='#4_Profile'>Get started by clicking here!</a>", unsafe_allow_html=True)
# st.markdown("<a href='#2_Quotes'>Comfort and confidence</a>", unsafe_allow_html=True)
# st.markdown("<a href='#3_Info_Hub'>Learn more about happy healthy lifestyles!</a>", unsafe_allow_html=True)

# DATA RETRIEVAL
# import pandas as pd 
# data = pd.read_csv("data.csv")
# st.write(data)