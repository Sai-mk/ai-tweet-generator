import streamlit as st
import requests

st.title("AI Brand Tweet Generator")

brand = st.text_input("Brand Name")
industry = st.text_input("Industry")
campaign = st.text_input("Campaign Objective")
product = st.text_area("Product Description")

API_KEY = st.secrets["OPENROUTER_API_KEY"]

def generate_tweets(prompt):

```
url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "openai/gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": prompt}
    ]
}

response = requests.post(url, headers=headers, json=data)
result = response.json()

return result["choices"][0]["message"]["content"]
```

if st.button("Generate Tweets"):

```
prompt = f"""
```

Generate 10 engaging Twitter tweets.

Brand Name: {brand}
Industry: {industry}
Campaign Objective: {campaign}
Product Description: {product}

Rules:

* Tweets must be short and catchy
* Include emojis
* Include hashtags
* Each tweet must be unique
  """

  tweets = generate_tweets(prompt)

  st.subheader("Generated Tweets")

  for tweet in tweets.split("\n"):
  if tweet.strip():
  st.write(tweet)
