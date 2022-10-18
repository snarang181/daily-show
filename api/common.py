import requests
import json

from dotenv import load_dotenv
import os

load_dotenv()
meta_auth_token = 'Bearer ' + os.environ.get('meta_api_token')

def format_cmd_msg(name : str) -> str: 
    """_summary_ : This function formats the message that contains all the commands that the user can use to interact with the bot.

    Args:
        name (str): The name of the user.

    Returns:
        str: The formatted message, containing all commands.
    """
    cmd = 'Hi ' + name + '! Here are the commands you can use: \n'
    cmd = cmd + '\t \u2022 /help - Get a list of commands \n'
    cmd = cmd + '\t \u2022 /joke - Read a joke \n'
    cmd = cmd + '\t \u2022 /price - Get latest prices \n'
    cmd = cmd + '\t \u2022 /weather - Get weather forecast \n'
    return cmd


def send_message_meta_api_call(phone_num : str , phone_num_id : str , message : str, name : str) -> None:
    """_summary_ : This function sends a message to the user using the Meta API.

    Args:
        phone_num (str): The phone number of the user.
        phone_num_id (str): The phone number ID of the user.
        message (str): The message to be sent to the user.
        name (str): The name of the user.

    Returns:
        _type_: None
    """
    global meta_auth_token    
    base_url = 'https://graph.facebook.com/v13.0/' + str(phone_num_id) + '/messages'
    headers = {'Authorization' : meta_auth_token, 'Content-Type': 'application/json'}
    body = {
        "messaging_product" : "whatsapp", "recipient_type" : "individual", "to" : str(phone_num) , "type" : "text" , "text" : {
            "preview_url" : False,
            "body" : str(message)
        }
    }
    r = requests.post(base_url, data=json.dumps(body), headers=headers)
    return None