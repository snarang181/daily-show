from email import message
from flask import Flask, request, render_template
from flask_cors import CORS
from flask_mail import Mail, Message
import os, requests, json
from dotenv import load_dotenv



load_dotenv()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def landing():
    data = request.get_json()
    return {'message': 'Hello, World! This is a private API used by the DailyShow WhatsappBot.'}, 200


@app.route('/callback', methods=['POST'])
def meta_callback():
    data = request.get_json()
    return {'message' : data}, 200