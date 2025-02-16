import streamlit as st
import os
import google.generativeai as genai
import random
from dotenv import load_dotenv

load_dotenv()

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

API_KEY = os.getenv("API_KEY")

genai.configure(api_key=f"{API_KEY}")

st.title("Quote Wall")

prompts = [
    "Directly list one positive quote related to life, beauty, motivation, confidence, and/or self-love. No need to write the category each quote is in, or number them. Do no use any copyrighted material.",
    "Directly list one inspiring quote about to moving on in life, health, motivation, self-confidence, and/or self-care. No need to write the category each quote is in, or number them. Do no use any copyrighted material.",
    "Directly list one positive quote on encouragement, body image, kindness, beauty, and/or positive-mindset. No need to write the category each quote is in, or number them. Do no use any copyrighted material.",
    "Directly list one encouraging quote about self-love, self-care, motivation, confidence, and/or overcoming life challenges. No need to write the category each quote is in, or number them. Do no use any copyrighted material.",
    "Directly list one uplifting quote about resilience, beauty of different forms, reducing stress, self-trust, and/or life. No need to write the category each quote is in, or number them. Do no use any copyrighted material.",
    "Directly list one comforting quote about life struggles, body image, not overworking, confidence, and/or kindness. No need to write the category each quote is in, or number them. Do no use any copyrighted material.",
    "Directly list one empowering quote about thinking positively, self-care, believing in yourself, exercising more, and/or overcoming life challenges. No need to write the category each quote is in, or number them. Do no use any copyrighted material.",
    "Directly list one motivating quote about how sleep contributes to beauty, motivation, how excerising more contributes to beauty, self-trust, and/or life struggles. No need to write the category each quote is in, or number them. Do no use any copyrighted material.",
    "Directly list one wise quote about self-love, health, trying not to overexert yourself, confidence, and/or overcoming hardships. No need to write the category each quote is in, or number them. Do no use any copyrighted material.",
    "Directly list one insightful quote about life, beauty, perseverance, self-confidence, and/or self-care. No need to write the category each quote is in, or number them."
]

# Generate and display quotes
def generate_quotes():
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(random.choice(prompts))  # Generate content from the model
        # Split the response by newlines to get individual quotes
        quotes = response.text.strip().split("\n")
        return quotes
    except Exception as e:
        st.error(f"Error generating quotes: {e}")
        return None

# Generate and display quotes
if st.button("Inspire me!"):
    quotes = generate_quotes()

    # Display the quotes
    if quotes:
        for quote in quotes:
            st.write(quote)