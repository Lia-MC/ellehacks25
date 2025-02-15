import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

secret_key = os.getenv("SECRET_KEY")
genai.configure(api_key=secret_key)

st.set_page_config(page_title="THE LIFE HACKERS", page_icon="✅", layout="centered")
st.title("Lifestyle and Skincare Recommendations")

name_input = st.text_input("Enter your name")
if name_input:
    st.write(f"Welcome, {name_input}!")

gender_input = st.selectbox("Select your gender", ["Male", "Female"])
age_input = st.slider("Select your age", 1, 100, 18)
text_input = st.text_area("Tell us about your diet, skin type, and lifestyle")
uploaded_file = st.file_uploader("Upload a photo of your skin condition", type=["jpg", "png"])

if st.button("Get Suggestions!"):
        
    if text_input and uploaded_file:
        prompt_text_skincare = f"Provide skincare recommendations for {gender_input} in the age of {age_input} with these details: {text_input}"
        prompt_text_mealplan = f"Provide meal plan recommendations for {gender_input} in the age of {age_input} with these details: {text_input}"

        prompt_condition_skincare = f"Provide skincare recommendations for {gender_input} in the age of {age_input} with these details: {uploaded_file}"
        prompt_condition_mealplan = f"Provide meal plan recommendations for {gender_input} in the age of {age_input} with these details: {uploaded_file}"

        model = genai.GenerativeModel("gemini-pro")
        response_text_skincare = model.generate_content(prompt_text_skincare)
        response_text_mealplan = model.generate_content(prompt_text_mealplan)
        response_condition_skincare = model.generate_content(prompt_condition_skincare)
        response_condition_mealplan = model.generate_content(prompt_condition_mealplan)

        st.title("Your Personalized Recommendations")
        st.subheader("Skincare Recommendations")
        st.write(response_text_skincare.text)
        st.write(response_condition_skincare.text)

        st.subheader("Meal Plan Recommendations")
        st.write(response_text_mealplan.text)
        st.write(response_condition_mealplan.text)

    else:
        st.warning("Please enter some details about your lifestyle and upload a photo of your skin condition to get personalized recommendations.")

