import streamlit as st
import requests

st.title("AI Brand Tweet Generator")

brand = st.text_input("Brand Name")
industry = st.text_input("Industry")
campaign = st.text_input("Campaign Objective")
product = st.text_area("Product Description")

if st.button("Generate Tweets"):

    prompt = f"""
    Generate 10 engaging tweets for a brand.

    Brand: {brand}
    Industry: {industry}
    Campaign: {campaign}
    Product: {product}

    Tweets should be short, engaging, and social-media friendly.
    """

    API_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-large"

    response = requests.post(API_URL, json={"inputs": prompt})
    try:
        result = response.json()
    except:
        st.write("AI model is waking up. Please click Generate Tweets again in a few seconds.")
        st.stop()

    st.subheader("Generated Tweets")
    if isinstance(result, list) and "generated_text" in result[0]:
        st.write(result[0]["generated_text"])
    else:
        st.write(result)
