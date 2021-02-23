import telebot

api_key = '1620071496:AAEHFRWv4UnU1b1wjTbrZ-x1Q3W5vpTibvM'

bot = telebot.TeleBot(api_key, parse_mode=None)  # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
    print(message)
    chat_id = message.chat.id
    print(chat_id)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)