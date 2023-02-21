import streamlit as st
import requests

st.title('Bitrix24 Webhook')

# Bitrix24 Webhook URL
url = "https://rosasprings.bitrix24.ru/rest/290/webhook/"

# Payload for the webhook
payload = {
    "event": "ONCRMPRODUCTADD",
    "handler": "https://rus77787-endpoint-endpoint-jfv8hn.streamlit.app/",
    "auth": "hdejdfhk7gazkb4ukj515towfpqhpnqm"
}

# Function to create the webhook
def create_webhook():
    response = requests.post(url, json=payload)
    st.write(response.text)

# Button to create the webhook
if st.button('Create Webhook'):
    create_webhook()
