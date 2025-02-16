import streamlit as st
import os
import google.generativeai as genai
import random
from dotenv import load_dotenv
import base64

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
            background-position: center;
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

API_KEY = os.getenv("API_KEY")

genai.configure(api_key=f"{API_KEY}")

st.markdown("<h1 class='title-highlight'>Quote Wall</h1>", unsafe_allow_html=True)

st.divider()

prompts = [
    "Directly list a bunch of random different positive quotes related to life, beauty, motivation, confidence, and/or self-love. No need to write the category each quote is in, or number them. Do no use any copyrighted material.",
    "Directly list a bunch of random different inspiring quotes about to moving on in life, health, motivation, self-confidence, and/or self-care. No need to write the category each quote is in, or number them. Do no use any copyrighted material.",
    "Directly list a bunch of random different positive quotes on encouragement, body image, kindness, beauty, and/or positive-mindset. No need to write the category each quote is in, or number them. Do no use any copyrighted material.",
    "Directly list a bunch of random different encouraging quotes about self-love, self-care, motivation, confidence, and/or overcoming life challenges. No need to write the category each quote is in, or number them. Do no use any copyrighted material.",
    "Directly list a bunch of random different uplifting quotes about resilience, beauty of different forms, reducing stress, self-trust, and/or life. No need to write the category each quote is in, or number them. Do no use any copyrighted material.",
    "Directly list a bunch of random different comforting quotes about life struggles, body image, not overworking, confidence, and/or kindness. No need to write the category each quote is in, or number them. Do no use any copyrighted material.",
    "Directly list a bunch of random different empowering quotes about thinking positively, self-care, believing in yourself, exercising more, and/or overcoming life challenges. No need to write the category each quote is in, or number them. Do no use any copyrighted material.",
    "Directly list a bunch of random different motivating quotes about how sleep contributes to beauty, motivation, how excerising more contributes to beauty, self-trust, and/or life struggles. No need to write the category each quote is in, or number them. Do no use any copyrighted material.",
    "Directly list a bunch of random different wise quotes about self-love, health, trying not to overexert yourself, confidence, and/or overcoming hardships. No need to write the category each quote is in, or number them. Do no use any copyrighted material.",
    "Directly list a bunch of random different insightful quotes about life, beauty, perseverance, self-confidence, and/or self-care. No need to write the category each quote is in, or number them."
]

# Generate and display quotes
def generate_quotes():
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(random.choice(prompts))  # Generate content from the model
        # Split the response by newlines to get individual quotes
        # quotes = response.text.strip().split("\n")
        quotes = [quote.strip() for quote in response.text.strip().split("\n") if quote.strip()]
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
            st.markdown(
                f"<p class='highlight' style='font-size: 20px;'>{quote}</p>",
                unsafe_allow_html=True
            )
