from email import message
from mimetypes import init
from flask import Flask, request, render_template
from flask_cors import CORS
from flask_mail import Mail, Message
import os, requests, json
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs
from api.decode_incoming_message import decipher_incoming_msg


load_dotenv()

app = Flask(__name__)




@app.route('/', methods=['GET'])
def landing():
    """ 
    This is the landing page for the app.
    Args: None
    Returns:
        render_template: The landing page for the app.
    """
    data = request.get_json()
    return {'message': 'Hello, World! This is a private API used by the DailyShow WhatsappBot.'}, 200


@app.route('/callback', methods = ['POST','GET'])
def receive_msg_endpoint():
    """_summary_: This is the endpoint that receives the incoming messages from the Whatsapp API.
    Args: None
    Returns:
        {dict}: Returns a statusCode 200 to signify that the message was received.
    """
    data = request.get_json()
    decipher_incoming_msg(data)
    return {'statusCode' : 200} 







#############  NOTE  #############
############# CALLBACK URL INITIAL API AUTH ######

# @app.route('/callback', methods=['GET'])
# def verification():
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
