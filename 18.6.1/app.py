import telebot
from config import TOKEN, keys
from extensions import ConversionException, PairConvetor

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = 'Для получения информации о курсах валют\n\
введите через пробел:\n <имя валют>\
<в какую валюту перевести>\
<количество конвертируемой валюты>\n\
Для того, чтобы получить список доступных валют\n\
вызовите: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Список досутпных валют: '
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConversionException('Введено не корректное количество параметров')

        quote, base, amount = values
        total_base_sum = PairConvetor.get_price(quote, base, amount)
    except ConversionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n {e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n {e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base_sum}'
        bot.send_message(message.chat.id, text)


bot.polling()
