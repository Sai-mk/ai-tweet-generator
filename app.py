import streamlit as st
from openai import OpenAI

st.title("AI Brand Tweet Generator")

brand = st.text_input("Brand Name")
industry = st.text_input("Industry")
campaign = st.text_input("Campaign Objective")
product = st.text_area("Product Description")

if st.button("Generate Tweets"):

    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    prompt = f"""
    You are a social media manager.

    Brand: {brand}
    Industry: {industry}
    Campaign Objective: {campaign}
    Product: {product}

    First analyze the brand voice in 3 bullet points.

    Then generate 10 engaging tweets matching that tone.
    Include promotional, witty, and informative tweets.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    st.write(response.choices[0].message.content)
