
from api.messages import send_all_commands_message, send_joke
from api.common import send_message_meta_api_call

def decide_response(phone_num : str, phone_num_id : str , message : str, name : str) -> None:
    """_summary_ : This function decides which function to call based on the message received from the user.

    Args:
        phone_num (str): The phone number of the user.
        phone_num_id (str): The phone number ID of the user.
        message (str): The message received from the user.
        name (str): The name of the user.
    """
    if 'help' in message:
        message = message.lower()
        send_all_commands_message(phone_num, phone_num_id, name)
    elif 'joke' in message:
        message = message.lower()
        send_joke(phone_num, phone_num_id, name)
    else: 
        send_message_meta_api_call(phone_num, phone_num_id, 'Hello ' + name + '! You said: ' + message, name)