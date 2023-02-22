import streamlit as st
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    st.write(request.json)
    return 'OK'

if __name__ == '__main__':
    app.run()


