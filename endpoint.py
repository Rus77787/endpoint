
import streamlit as st
import requests

BITRIX24_WEBHOOK_URL = "http://endpoint.streamlit.app"

st.title("New Deals Dashboard")

def get_new_deals():
    response = requests.get(BITRIX24_WEBHOOK_URL)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to retrieve new deals.")

new_deals = get_new_deals()

if new_deals:
    st.write(f"Received {len(new_deals)} new deals!")
    for deal in new_deals:
        st.write(f"Deal ID: {deal['id']}")
        st.write(f"Deal Title: {deal['title']}")
        st.write(f"Deal Value: {deal['value']}")
else:
    st.write("No new deals received.")



