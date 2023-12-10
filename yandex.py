import telebot
import requests

TOKEN = '1693269053:AAFz2VNZhzKQHQA8laNCH3B0TLpz4QQdLWg'
# Here is the token for bot Azmuka @AzmukaBot:
# 1693269053:AAFz2VNZhzKQHQA8laNCH3B0TLpz4QQdLWg

YANDEX_TOKEN = 'y0_AgAAAABR2QGiAADLWwAAAADjyvy_4jNywNthRsO5PHTsIPOSpToCxrw'
HOST_YANDEX_DISK = 'https://cloud-api.yandex.net:443'

bot = telebot.TeleBot(TOKEN)


def create_folder(message):
    path = message.text
    headers = {'Authorization': 'OAuth %s' % YANDEX_TOKEN}
    request_url = HOST_YANDEX_DISK + '/v1/disk/resources?path=%s' % path
    response = requests.put(url=request_url, headers=headers)
    if response.status_code == 201:
        bot.reply_to(message, "Я создал папку %s" % path)
    else:
        bot.reply_to(message, '\n'.join(["Произошла ошибка. Текст ошибки: ", response.text]))



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет, я учебный бот')
    bot.send_message(message.chat.id, 'Привет')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Я знаю две команды  start и help')


@bot.message_handler(commands=['create_folder'])
def send_create_folder(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, 'Введите название папки')
    bot.register_next_step_handler(msg, create_folder)


if __name__ == '__main__':
    print('Bot is running')
    bot.polling()
