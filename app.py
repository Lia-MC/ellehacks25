import streamlit as st
import google.generativeai as genai

st.title("Lifestyle and Skincare Recommendations")

name_input = st.text_input("Enter your name")
if name_input:
    st.write(f"Welcome, {name_input}!")

gender_input = st.selectbox("Select your gender", ["Biological Male", "Biological Female"])
age_input = st.slider("Select your age", 1, 100, 18)
text_input = st.text_area("Tell us about your diet, skin type, and lifestyle")
uploaded_file = st.file_uploader("Upload a photo of your skin for more accurate recommendations (optional)", type=["jpg", "png"])

if st.button("Get Suggestions!"):
    if text_input and not uploaded_file:
        prompt_text = f"Provide skincare and meal plan recommendations for someone with these details: {text_input}"

        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt_text)

        st.subheader("Your Personalized Recommendations")
        st.write(response.text)
        
    elif text_input and uploaded_file:
        prompt_text = f"Provide skincare and meal plan recommendations for someone with these details: {text_input}"
        prompt_image = f"Provide skincare and meal plan recommendations for someone with these details: {uploaded_file}"

        model = genai.GenerativeModel("gemini-pro")
        response_text = model.generate_content(prompt_text)
        response_image = model.generate_content(prompt_image)


        st.subheader("Your Personalized Recommendations")
        st.write(response_text.text)
        st.write(response_image.text)
    
    else:
        st.warning("Please enter some details about your diet, skin type, and lifestyle")

