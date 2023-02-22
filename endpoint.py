!pip install flask
import streamlit as st
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bitrix24-webhook', methods=['POST'])
def bitrix24_webhook():
    data = request.get_json()
    st.write(data)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)


