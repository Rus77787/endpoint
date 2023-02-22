import streamlit as st
from streamlit.web.server.websocket_headers import _get_websocket_headers
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
report_ctx = _getwebsocket_headers()
if report_ctx is not None:
    request_body = report_ctx.request_body_bytes
    if request_body:
        handle_webhook(request_body.decode('utf-8'))
        st.success("Webhook request handled successfully.")
else:
    st.write("Listening for incoming webhook requests...")

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

