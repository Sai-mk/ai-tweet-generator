import streamlit as st
import random

st.title("AI Brand Tweet Generator")

brand = st.text_input("Brand Name")
industry = st.text_input("Industry")
campaign = st.text_input("Campaign Objective")
product = st.text_area("Product Description")

if st.button("Generate Tweets"):

    st.subheader("Brand Voice")

    tone = random.choice([
        "fun and conversational",
        "bold and motivational",
        "informative and engaging",
        "witty and playful"
    ])

    audience = f"people interested in {industry}"
    themes = f"{campaign}, product highlights, trending topics"

    st.write(f"**Tone:** {tone}")
    st.write(f"**Audience:** {audience}")
    st.write(f"**Themes:** {themes}")

    st.subheader("Generated Tweets")

    tweets = [
        f"{brand} is bringing something exciting to the {industry} world. Stay tuned! 🚀",
        f"Looking for the best in {industry}? {brand} has you covered.",
        f"{campaign} just got better with {brand}! Don’t miss out.",
        f"Why everyone is talking about {brand} in the {industry} space 👀",
        f"Upgrade your experience with {brand}.",
        f"The future of {industry} starts with {brand}.",
        f"Thousands already trust {brand}. Will you?",
        f"{brand} is redefining innovation in {industry}.",
        f"Ready to explore something new? {brand} is here.",
        f"Your journey with {brand} starts today."
    ]

    random.shuffle(tweets)

    for i, tweet in enumerate(tweets, start=1):
        st.write(f"{i}. {tweet}")
