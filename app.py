import streamlit as st

st.title("AI Brand Tweet Generator")

brand = st.text_input("Brand Name")
industry = st.text_input("Industry")
campaign = st.text_input("Campaign Objective")
product = st.text_area("Product Description")

if st.button("Generate Tweets"):

    st.subheader("Brand Voice")

    st.write(f"""
Tone: Friendly and engaging
Audience: Customers interested in {industry}
Themes: {campaign}, product highlights, brand awareness
""")

    st.subheader("Generated Tweets")

    tweets = [
        f"{brand} is changing the game in {industry}. Discover more today!",
        f"Looking for the best in {industry}? {brand} has you covered.",
        f"Introducing something exciting from {brand}! Stay tuned.",
        f"Upgrade your experience with {brand}. #Innovation",
        f"Did you know? {brand} is leading trends in {industry}.",
        f"Don't miss out! {brand} brings you the best in {industry}.",
        f"Experience quality and innovation with {brand}.",
        f"Your journey with {brand} starts today!",
        f"Join thousands who trust {brand} in the {industry} space.",
        f"Ready to explore? Discover what {brand} offers today!"
    ]

    for tweet in tweets:
        st.write("•", tweet)
