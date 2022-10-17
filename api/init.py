from email import message
from mimetypes import init
from flask import Flask, request, render_template
from flask_cors import CORS
from flask_mail import Mail, Message
import os, requests, json
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs
from api.messages import decide_response


load_dotenv()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def landing():
    data = request.get_json()
    return {'message': 'Hello, World! This is a private API used by the DailyShow WhatsappBot.'}, 200


@app.route('/callback', methods = ['POST','GET'])
def receive_msg():
    data = request.get_json()
    print(data)
    init_arr = data['entry'][0]['changes']
    phone_num_id = init_arr[0]['value']['metadata']['phone_number_id']
    phone_num = init_arr[0]['value']['messages'][0]['from']
    name = init_arr[0]['value']['contacts'][0]['profile']['name']
    user_msg = init_arr[0]['value']['messages'][0]['text']['body']
    decide_response(phone_num, phone_num_id, user_msg, name)
    return {'statusCode' : 200}

# @app.route('/callback', methods=['GET'])
# def verification():
#     print('Verification is called')
#     try: 
#         args = request.args
#         challenge = args.get('hub.challenge')
#         mode = args.get('hub.mode')
#         token = args.get('hub.verify_token')
#         if (mode == 'subscribe' and token == os.environ.get('meta_token')):
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
