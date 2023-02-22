import streamlit as st
import requests
import json

st.title('Bitrix24 Webhook')

# Bitrix24 Webhook URL
url = "https://rosasprings.bitrix24.ru/rest/290/webhook/"

# Payload for the webhook
payload = {
    "event": "ONCRMPRODUCTADD",
    "handler": "https://endpoint.streamlit.app/",
    "auth": "hdejdfhk7gazkb4ukj515towfpqhpnqm"
}

data = { 'name': 'This is an example for webhook' }
requests.post(webhook_url, data=json.dumps(data), headers=payload)


