import streamlit as st
import requests

st.title("AI Brand Tweet Generator")

brand = st.text_input("Brand Name")
industry = st.text_input("Industry")
campaign = st.text_input("Campaign Objective")
product = st.text_area("Product Description")

API_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-large"

headers = {
    "Authorization": "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"
}

def generate_tweets(prompt):
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    return response.json()

if st.button("Generate Tweets"):

    prompt = f"""
Generate 10 engaging tweets for brand {brand}.

Industry: {industry}
Campaign: {campaign}
Product: {product}

Each tweet should be short and engaging.
"""

    result = generate_tweets(prompt)

    st.subheader("Generated Tweets")

    st.write(result)
