import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import base64

load_dotenv()

st.set_page_config(page_title="CUTIS", layout="centered")

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
        /* Highlight effect */
        .highlight {{
            background-color: #fff4dd;
            padding: 5px 10px;
            border-radius: 5px;
            display: inline-block;
        }}
        /* Title Styling */
        .title-highlight {{
            background-color: #fff4dd;
            padding: 2px 15px; /* Reduced height */
            border-radius: 5px;
            
            text-align: center;
        }}
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)

set_background('bg_image_updated2.png')

secret_key = os.getenv("SECRET_KEY")
genai.configure(api_key=secret_key)

# st.set_page_config(page_title="CUTIS", layout="centered")

# st.image("title_art.png", use_column_width=True)

st.markdown("<h1 class='title-highlight'>Cutis</h1>", unsafe_allow_html=True)
st.divider()

st.markdown("<p class='highlight' style='font-size: 20px;'>Enter your name</p>", unsafe_allow_html=True)
name_input = st.text_input("")

if name_input:
    st.markdown(f"<p class='highlight' style='font-size: 20px;'>Welcome, {name_input}!</p>", unsafe_allow_html=True)
    # st.write(f"Welcome, {name_input}!")

st.markdown("<p class='highlight' style='font-size: 20px;'>Select your gender:</p>", unsafe_allow_html=True)
gender_input = st.selectbox("", ["Male", "Female"])

st.markdown("<p class='highlight' style='font-size: 20px;'>Select your age:</p>", unsafe_allow_html=True)
age_input = st.number_input("", min_value=1, max_value=100, value="min", step=1)
# age_input = st.slider("", 1, 100, 18)

st.markdown("<p class='highlight' style='font-size: 20px;'>Tell us about your diet, skin type, and lifestyle:</p>", unsafe_allow_html=True)
text_input = st.text_area("")

st.markdown("<p class='highlight' style='font-size: 20px;'>Upload a photo of your skin condition:</p>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["jpg", "png"])

# gender_input = st.selectbox("Select your gender", ["Male", "Female"])
# age_input = st.slider("Select your age", 1, 100, 18)
# text_input = st.text_area("Tell us about your diet, skin type, and lifestyle")
# uploaded_file = st.file_uploader("Upload a photo of your skin condition", type=["jpg", "png"])

if st.button("Get Suggestions!"):
        
    if text_input and uploaded_file:
        prompt = f"Provide skincare and meal plan recommendations for {gender_input} in the age of {age_input} with these details: {text_input} and {uploaded_file}"

        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)

        st.markdown(f"<div class='highlight' style='font-size: 20px;'>{response.text}</div>",unsafe_allow_html=True)

        # prompt_text_skincare = f"Provide skincare recommendations for {gender_input} in the age of {age_input} with these details: {text_input}"
        # prompt_text_mealplan = f"Provide meal plan recommendations for {gender_input} in the age of {age_input} with these details: {text_input}"

        # prompt_condition_skincare = f"Provide skincare recommendations for {gender_input} in the age of {age_input} with these details: {uploaded_file}"
        # prompt_condition_mealplan = f"Provide meal plan recommendations for {gender_input} in the age of {age_input} with these details: {uploaded_file}"

        # model = genai.GenerativeModel("gemini-pro")
        # response_text_skincare = model.generate_content(prompt_text_skincare)
        # response_text_mealplan = model.generate_content(prompt_text_mealplan)
        # response_condition_skincare = model.generate_content(prompt_condition_skincare)
        # response_condition_mealplan = model.generate_content(prompt_condition_mealplan)

        # st.title("Your Personalized Recommendations")
        # st.subheader("Skincare Recommendations")
        # st.write(response_text_skincare.text)
        # st.write(response_condition_skincare.text)

        # st.subheader("Meal Plan Recommendations")
        # st.write(response_text_mealplan.text)
        # st.write(response_condition_mealplan.text)

    else:
        st.warning("Please enter some details about your lifestyle and upload a photo of your skin condition to get personalized recommendations.")