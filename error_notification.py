import telebot

def send_error_to_telegramm(text):
    """Func send messages in telegram"""

    print(text)
    try:

        
        bot_token = 'YOUR_BOT_TOKEN_HERE'

        
        bot = telebot.TeleBot(bot_token)

        
        group_chat_id = your_group_chat_id 

        bot.send_message(group_chat_id, text)
    except Exception as e:
        print('Error in file_name. Error : ', e)
        raise


if __name__ == '__main__':

    try:
        from file_name import file_name_test

        file_name_test()
    except Exception as e:
        send_error_to_telegramm(f'Error in file_name. Error : {e}')   
