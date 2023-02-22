import streamlit as st
import requests

st.title('Bitrix24 Webhook')

# Bitrix24 Webhook URL
url = "https://rosasprings.bitrix24.ru/rest/290/webhook/"

# Payload for the webhook
payload = {
    "event": "ONCRMPRODUCTADD",
    "handler": "https://rus77787-endpoint-endpoint-jfv8hn.streamlit.app",
    "auth": "hdejdfhk7gazkb4ukj515towfpqhpnqm"
}

# Function to create the webhook
def create_webhook():
    response = requests.post(url, json=payload)
    st.write(response.text)

# Button to create the webhook
if st.button('Create Webhook'):
    create_webhook()

    
    st.title('Bitrix24 Webhook Handler')

@st.cache(allow_output_mutation=True)
def get_deals():
    return []

deals = get_deals()

# Endpoint for the webhook handler
@st.cache(allow_output_mutation=True)
def webhook_handler(request):
    data = request.get_json()
    if data['event'] == 'ONCRMPRODUCTADD':
        deal = data['data']['FIELDS']
        deals.append(deal)
        st.write(deals)

if __name__ == '__main__':
    st.server.set_app(webhook_handler)
    st.write('Listening for Bitrix24 webhook events...')
