import streamlit as st
import requests
import json
from bitrix24.bitrix24 import Bitrix24


C_REST_CLIENT_ID = 'local.63f5dac3a863a8.66886970'
C_REST_CLIENT_SECRET = 'pE3n3dSnMTUSO7BhQafuZ0dxJdjRYbaoi0uWHAnlTq0RRt2iKI'

# Define the endpoint URL for the webhook
BITRIX_WEBHOOK_URL = "http://endpoint.streamlit.app"
TOKEN = 'hdejdfhk7gazkb4ukj515towfpqhpnqm'

bx24 = Bitrix24(
    'https://rosasprings.bitrix24.ru/rest/',
    TOKEN
)

bx24.call(
    'event.bind',
    {
        'event': 'ONCRDEALADD',
        'handler': 'https://endpoint.streamlit.app/'
    }
)


# Define the event type and data to be sent to the webhook
EVENT_TYPE = 'ONCRMDEALADD'

# Create a button in Streamlit to trigger the webhook
if st.button('Trigger Webhook'):
    # Send a POST request to the webhook URL with the event type and data
    response = requests.post(BITRIX_WEBHOOK_URL, json={'event_type': EVENT_TYPE})
    print(response.text)
    # Check the status code of the response to ensure the webhook was successful
    if response.status_code == 200:
        st.success('Webhook triggered successfully!')
        print
    else:
        st.error('Failed to trigger webhook.')
        


        

