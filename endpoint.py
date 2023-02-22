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

data = request.get_json()
if data['event'] == 'ONCRMPRODUCTADD':
    deal = data['data']['FIELDS']
    deals.append(deal)
    st.write(deals)
        

requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

# Button to create the webhook
if st.button('Create Webhook'):
    create_webhook()


