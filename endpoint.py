import streamlit as st
import requests
import json



C_REST_CLIENT_ID = 'local.63f7262142b291.82315904'
C_REST_CLIENT_SECRET = 'UHVUSyXlPzaTSASTq5MjOctmz48qsQaEs2FNwW02kaQeXp31F3'
BITRIX_WEBHOOK_URL = "https://endpoint.streamlit.app"


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
        


        

