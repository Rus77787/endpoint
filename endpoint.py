import streamlit as st
import requests
import json

# Set up the webhook endpoint URL
webhook_url = "https://endpoint.streamlit.app/"

# Define a function to handle incoming webhook requests
def handle_webhook(data):
    # Parse the data from the webhook request
    payload = json.loads(data)
    
    # Check if the payload contains a new deal
    if payload.get('event') == 'ONCRMDEALADD':
        deal_id = payload['data'][0]['ID']
        deal_title = payload['data'][0]['TITLE']
        st.write(f"New deal added: {deal_title} (ID: {deal_id})")

# Set up the Streamlit app
st.title("Bitrix24 Webhook Endpoint")

# Listen for incoming webhook requests
if st._is_running_with_streamlit:
    if st._is_in_session():
        st.write("Listening for incoming webhook requests...")
        request_body = st._request_body
        if request_body:
            handle_webhook(request_body)
            st.success("Webhook request handled successfully.")
    
    # Display a form to test the webhook endpoint
    st.subheader("Test the webhook endpoint")
    deal_title = st.text_input("Deal title")
    if st.button("Simulate new deal"):
        payload = {
            "event": "ONCRMDEALADD",
            "data": [{
                "ID": "123",
                "TITLE": deal_title
            }]
        }
        response = requests.post(webhook_url, json=payload)
        if response.ok:
            st.success("Webhook request sent successfully.")
        else:
            st.error("Failed to send webhook request.")
