import streamlit as st

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
