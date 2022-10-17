from email import message
from flask import Flask, request, render_template
from flask_cors import CORS
from flask_mail import Mail, Message
import os, requests, json
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs



load_dotenv()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def landing():
    data = request.get_json()
    return {'message': 'Hello, World! This is a private API used by the DailyShow WhatsappBot.'}, 200


@app.route('/callback', methods = ['POST','GET'])
def receive_msg():
    print('Message received')
    print(request.get_json())
    print(request.args)


# @app.route('/callback', methods=['GET'])
# def verification():
#     print('Verification is called')
#     try: 
#         args = request.args
#         challenge = args.get('hub.challenge')
#         mode = args.get('hub.mode')
#         token = args.get('hub.verify_token')
#         if (mode == 'subscribe' and token == 'whatsapp_daily_show'):
#             print('Verification successful')
#             return challenge
#         else:
#             return {
#                 'statusCode': 403,
#                 'body': challenge
#             }
#     except Exception as e:
#         print('Faced exception')
#         print(str(e))
#         return {
#                     'statusCode': 403,
#                     'body':"lol"
#                 }
