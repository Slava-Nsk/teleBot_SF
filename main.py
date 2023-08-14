import telebot
from values import values
from extensions import APIException, Converter
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f"""Приветствую на борту бота!
Данный бот может конвертировать валюту по актуальному курсу.
Для конвертации валюты, отправь запрос следующего формата:
<валюта> <валюта, в которую будем переводить> <количество валюты>

Пример запроса:
доллар евро 500

Список доступных комманд: /help\nСписок доступных валют: /values""")

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, f"""Для конвертации валюты, отправь запрос следующего формата:
<валюта> <валюта, в которую будем переводить> <количество валюты>

Пример запроса:
доллар евро 500

Список доступных валют: /values""")

@bot.message_handler(commands=['values'])
def values_message(message):
    text = 'Доступные валюты:'
    for i in values.keys():
        text = "\n   • ".join((text, i)) + ' (' + (values[i]) + ')'
    bot.send_message(message.chat.id, text)

@bot.message_handler()
def input_message(message):
    input_text_list = message.text.lower().split()
    try:
        result = Converter.get_price(input_text_list)
    except APIException as e:
        bot.send_message(message.chat.id,  f"""Возникла ошибка:\n{e}\n\nЕсли нужна помощь, нажми /help""")
    else:
        bot.send_message(message.chat.id, f"""{input_text_list[2]} {values[input_text_list[0]]} в {values[input_text_list[1]]} = {result:.2f} {values[input_text_list[1]]}""")

bot.polling(none_stop=True)
