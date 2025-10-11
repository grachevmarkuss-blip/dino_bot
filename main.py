import telebot

TOKEN = '8209222535:AAEiYZXNWfjPEe0l3YJMrwzLJW-RCvVgVOc'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_hay(message):
    bot.send_message(message.chat.id,'привет я твой бот я не умею нечего!')

@bot.message_handler(commands=['learn'])
def handle_learning(message):
    bot.send_message(message.chat.id,'Обучения сейчас начнётся!')

@bot.message_handler(func=lambda message: True)
def message_all(message):
    if message.text.lower() == 'как тебя зовут?':
        bot.send_message(message.chat.id,'......От багдада до Бухоры... всее знают моё имя.... яя ХАджана Средин сам себе господин никогда не умру не когда ни совру')
    elif message.text.lower() == 'как дела?':
        bot.send_message(message.chat.id,'как всегда очень')
    elif message.text.lower() == 'есть будешь?':
        bot.send_message(message.chat.id,'я недавно поел')
    elif message.text.lower() == 'а что ты поел?':
        bot.send_message(message.chat.id,'3 гб памяти с приправой из твоих вирусов с пк так что не благодари')
    else:
        bot.send_message(message.chat.id,message.text)



if __name__ == '__main__':
    bot.polling(none_stop=True)
