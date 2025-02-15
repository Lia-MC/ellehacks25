import streamlit as st

st.title("Home")
st.divider()

st.write("Welcome!")

skinDisease = "Acne"

from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works",
)

print(response.text)


# DATA INPUT
# name = st.text_input("Your name:")
# age = st.text_input("Your age:")
# skin_conditions = st.text_input("Your skin conditions:")

# DATA RETRIEVAL
# import pandas as pd 
# data = pd.read_csv("data.csv")
# st.write(data)

# MULTIPLE PAGES
# link_button