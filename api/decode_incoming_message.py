import requests
import json
from dotenv import load_dotenv
from api.decide_bot_response import decide_response

def decipher_incoming_msg(json_incoming_data : dict) -> None: 
    """_summary_ : This function deciphers the incoming message and calls the appropriate function to handle the message.

    Args:
        json_incoming_data (dict): The incoming message from the Whatsapp API.

    Returns:
        _type_: None
    """
    try:
        print(json_incoming_data)
        init_arr = json_incoming_data['entry'][0]['changes']
        phone_num_id = init_arr[0]['value']['metadata']['phone_number_id']
        phone_num = init_arr[0]['value']['messages'][0]['from']
        name = init_arr[0]['value']['contacts'][0]['profile']['name']
        user_msg = init_arr[0]['value']['messages'][0]['text']['body']
        decide_response(phone_num, phone_num_id, user_msg, name)
    except Exception as e:
        print('Repeated messages incoming')
    return None
    