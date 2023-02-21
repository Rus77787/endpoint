import streamlit as st
import requests

st.title('Bitrix24 Webhook')

# Bitrix24 Webhook URL
url = "https://your-bitrix24-url/rest/1/webhook/"

# Payload for the webhook
payload = {
    "event": "ONCRMPRODUCTADD",
    "handler": "https://your-streamlit-url/webhook-handler",
    "auth": "your-authentication-code"
}

# Function to create the webhook
def create_webhook():
    response = requests.post(url, json=payload)
    st.write(response.text)

# Button to create the webhook
if st.button('Create Webhook'):
    create_webhook()
