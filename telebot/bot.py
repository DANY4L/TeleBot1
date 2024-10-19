
import telebot
from constans import API_KEY

bot = telebot.TeleBot(API_KEY, parse_mode=None)

CHANNEL_USERNAME = 'midway'

def is_user_member(user_id):
    try:
        member = bot.get_chat_member(chat_id=f"@{CHANNEL_USERNAME}", user_id=user_id)
        if member.status in ['member', 'administrator', 'creator']:
            return True
    except Exception as e:
        print(f"Error: {e}")
    return False

@bot.message_handler(commands=['start', 'hello'])
def send_welcome_message(msg):
    user_id = msg.from_user.id
    if not is_user_member(user_id):
        bot.send_message(msg.chat.id, f"You need to join the channel first. @{CHANNEL_USERNAME}")
    else:
        bot.send_message(msg.chat.id,f"welcome to bot{msg.form.user.first_name}")

    bot.reply_to(msg, 'Hello! This is a Telegram bot written in Python')


@bot.message_handler(content_types=['photo', 'sticker'])
def send_content_message(msg):
    bot.reply_to(msg, "That's not a text message!")


bot.polling()