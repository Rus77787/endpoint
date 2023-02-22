import streamlit as st
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.get_json()
    st.write(data)
    return 'success'

if __name__ == '__main__':
    app.run()


