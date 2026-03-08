import streamlit as st

st.title("AI Brand Tweet Generator")

brand = st.text_input("Brand Name")
industry = st.text_input("Industry")
campaign = st.text_input("Campaign Objective")
product = st.text_area("Product Description")

if st.button("Generate Tweets"):

    st.subheader("Brand Voice")

    st.write("""
Tone: Engaging and brand specific  
Audience: Target customers of the brand  
Themes: Product promotion, trends, engagement
""")

    st.subheader("Generated Tweets")

    tweets = [
        "Tweet 1 related to the brand",
        "Tweet 2 engaging customers",
        "Tweet 3 promoting the product",
        "Tweet 4 with witty brand tone",
        "Tweet 5 informative tweet",
        "Tweet 6 promotional tweet",
        "Tweet 7 engaging tweet",
        "Tweet 8 creative tweet",
        "Tweet 9 brand awareness tweet",
        "Tweet 10 call to action tweet"
    ]

    for tweet in tweets:
        st.write("- ", tweet)
