import streamlit as st

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

st.title("Self Care")
st.divider()

st.write("It's important to care for your health for a happier healthier life!")
st.write("Here are some tips to make that happen:")

st.header("1. Sleep :star2:")
st.write("A good night sleep is essential to keeping to health, including skin health")

st.header("2. Eat healthy :herb:")
st.write("You are what you eat! Not exactly... but the less oily things you eat, the less skin irritations you will have")

st.header("3. Exercise :woman-running:")
st.write("Exercise helps you feel better, mentally and physically")

st.header("4. Practice good hygiene :shower:")
st.write("It's important to shower and wash your face every night")