import streamlit as st
import base64

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

st.markdown("<h1 class='title-highlight'>Self Care</h1>", unsafe_allow_html=True)
st.divider()

tips = [
    ("Sleep", "A good night sleep is essential to keeping to health, including skin health", "&#11088;"),
    ("Eat healthy", "You are what you eat! Not exactly... but the less oily things you eat, the less skin irritations you will have", "&#127807;"),
    ("Exercise", "Exercise helps you feel better, mentally and physically", "&#127939;"),
    ("Practice good hygiene", "It's important to shower and wash your face every night", "	&#128703;")
]

st.markdown("<p class='highlight' style='font-size: 20px;'>It's important to care for your health for a happier healthier life!</p>", unsafe_allow_html=True)
st.markdown("<p class='highlight' style='font-size: 20px;'>Here are some tips to make that happen:</p>", unsafe_allow_html=True)

for i, (title, description, emoji) in enumerate(tips, start=1):
    st.markdown(f"<p class='highlight' style='font-size: 24px;'>{i}. {title} {emoji}</p>", unsafe_allow_html=True)
    st.markdown(f"<p class='highlight' style='font-size: 20px;'>{description}</p>", unsafe_allow_html=True)

# st.write("It's important to care for your health for a happier healthier life!")
# st.write("Here are some tips to make that happen:")

# st.header("1. Sleep :star2:")
# st.write("A good night sleep is essential to keeping to health, including skin health")

# st.header("2. Eat healthy :herb:")
# st.write("You are what you eat! Not exactly... but the less oily things you eat, the less skin irritations you will have")

# st.header("3. Exercise :woman-running:")
# st.write("Exercise helps you feel better, mentally and physically")

# st.header("4. Practice good hygiene :shower:")
# st.write("It's important to shower and wash your face every night")