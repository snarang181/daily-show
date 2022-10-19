from api.messages import send_all_commands_message, send_joke, send_movie_message, send_weather_message, send_news_message, send_stocks_message
from api.common import send_message_meta_api_call

def decide_response(phone_num : str, phone_num_id : str , message : str, name : str) -> None:
    """_summary_ : This function decides which function to call based on the message received from the user.

    Args:
        phone_num (str): The phone number of the user.
        phone_num_id (str): The phone number ID of the user.
        message (str): The message received from the user.
        name (str): The name of the user.
    """
    if 'help' in message.lower():
        send_all_commands_message(phone_num, phone_num_id, name)
    elif 'joke' in message.lower():
        send_joke(phone_num, phone_num_id, name)
    elif 'weather' in message.lower():
        city_name = message.lower().replace('weather', '')
        city_name = city_name.strip()
        if city_name == '':
            send_message_meta_api_call(phone_num, phone_num_id, 'Please enter the city name.', name)
        else:    
            send_weather_message(phone_num, phone_num_id, name, city_name)
    elif 'news' in message.lower():
        send_message_meta_api_call(phone_num, phone_num_id, 'Processing the latest news for you ' + name, name)
        send_news_message(phone_num, phone_num_id, name)
    elif 'movie' in message.lower():
        send_movie_message(phone_num, phone_num_id, name)
    elif 'price' in message.lower():
        stock_name = message.lower().replace('price', '')
        stock_name = stock_name.strip()
        if stock_name == '':
            send_message_meta_api_call(phone_num, phone_num_id, 'Please enter the stock name.', name)
        else: 
            send_stocks_message(phone_num, phone_num_id, name, stock_name)
    else: 
        #Echo the message back to the user
        send_message_meta_api_call(phone_num, phone_num_id, 'Hello ' + name + '! You said: ' + message, name)