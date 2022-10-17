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


@app.route('/callback', methods=['GET'])
def verification():
    print('Verification is called')
    data = request.get_json()
    print(request.GET.get('hub.mode'))
    print(request.GET.get('hub.challenge'))
    print(request.GET.get('hub.verify_token'))
    return request.GET.get('hub.challenge'), 200

    # try:
    #     mode = event['queryStringParameters']['hub.mode']
    #     challenge = event['queryStringParameters']['hub.challenge']
    #     token = event['queryStringParameters']['hub.verify_token']
    #     if(mode == 'subscribe' and token == 'manmeet@sammy'):
    #             return {
    #                 'statusCode': 200,
    #                 'body': challenge
    #             }
    #     else:
    #         return {
    #             'statusCode': 403,
    #             'body': challenge
    #         }
    # except Exception as e:
    #     print('Faced exception')
    #     print(str(e))
    #     return {
    #                 'statusCode': 403,
    #                 'body':"lol"
    #             }
