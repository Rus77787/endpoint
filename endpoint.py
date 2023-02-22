import streamlit as st
import requests

# Define the endpoint URL for the webhook
BITRIX_WEBHOOK_URL = "http://endpoint.streamlit.app"
TOKEN = 'hdejdfhk7gazkb4ukj515towfpqhpnqm'

# Define the event type and data to be sent to the webhook
EVENT_TYPE = 'ONCRMDEALADD'
EVENT_DATA = {'deal_name': 'ID'}

# Create a button in Streamlit to trigger the webhook
if st.button('Trigger Webhook'):
    # Send a POST request to the webhook URL with the event type and data
    response = requests.post(BITRIX_WEBHOOK_URL, json={'event_type': EVENT_TYPE, 'event_data': EVENT_DATA})
    
    # Check the status code of the response to ensure the webhook was successful
    if response.status_code == 200:
        st.success('Webhook triggered successfully!')
        
        
        # Get the JSON data from the request
        data = json.loads(request.data)
        # Check the event type
        if data['event_type'] == EVENT_TYPE:
            # Get the data for the new deal event
            deal_data = data['event_data']

            # Display the deal data in Streamlit
            st.write('New deal created:')
            st.write(deal_data)
            
            
    else:
        st.error('Failed to trigger webhook.')
