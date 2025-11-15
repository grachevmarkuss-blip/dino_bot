import telebot
import json
import random

TOKEN = '8209222535:AAEiYZXNWfjPEe0l3YJMrwzLJW-RCvVgVOc'

bot = telebot.TeleBot(TOKEN)

with open("user_data.json", "r", encoding='utf8') as file:
    user_data = json.load(file)

@bot.message_handler(commands=['start'])
def handle_hay(message):
    bot.send_message(message.chat.id,'привет я твой бот я не умею нечего! Если что пиши команду /help')

@bot.message_handler(commands=['addword'])
def handle_addwording(message):
    global user_data
    chat_id = message.chat.id
    user_dict = user_data.get(chat_id, {})

    words = message.text.split()[1:]
    if len(words) == 2:
        word, translation = words[0].lower(), words[1].lower()
        user_dict[word] = translation

        user_data[chat_id] = user_dict

        with open("user_data.json", "w", encoding='utf8') as file:
            json.dump(user_data, file, ensure_ascii=False, indent=4)

        bot.send_message(chat_id, f"Слово '{word}' добавлено в словарь")
    else:
        bot.send_message(chat_id, "Произошла но не бойтесь меня починит разраб или же попробуйте ещё раз")

@bot.message_handler(commands=['learn'])
def handle_learning(message):
    user_words = user_data.get(str(message.chat.id), {})

    words_number = int(message.text.split()[1])

    ask_transation(message.chat_id, user_words, words_number)
    if len(user_data.get(str(message.chat.id)).items()) > 0:
        bot.send_message(message.chat.id, 'Обучения сейчас начнётся!')
        user_words = user_data.get(str(message.chat.id), {})
        random_word = random.choice(list(user_words.keys()))
        bot.send_message(message.chat.id, f"{random_word}")
    else:
        bot.send_message(str(message.chat.id), "у вас пуст словарь")

def ask_transation(chat_id, user_words, words_left):
   if words_left > 0:
       word = random.choice(list(user_words.keys()))
       translation = user_words[word]
       bot.send_message(chat_id, f'Напиши перевод слова "{word}".')

       bot.register_next_step_handler_by_chat_id(chat_id, check_translation, words_left, translation)
   else:
       bot.send_message(chat_id, "Урок окончен с вас 5 тыщ до завтра >:)")


def check_translation(message, expected_translation, words_left):
    user_translation = message.text.strip().lower()
    if user_translation == expected_translation.lower():
        bot.send_message(message.chat_id, 'Тебе просто повезло!!!')
    else:
        bot.send_message(message.chat_id, f'ХА слабачьё не умеешь ничего даже эээ ну   КОРОЧЕ НЕЧЕГО НЕ УМЕЕШЬ 2 в журнал за год я твоя училка под прикрытием а правильный ответ "{expected_translation}"')

    ask_transation(message.chat_id, user_translation, user_data[str(message.chat.id)], words_left)



@bot.message_handler(commands=['help'])
def handle_helping(message):
    bot.send_message(message.chat.id,'1. Этот бот создан для изучения англиского языка ;')
    bot.send_message(message.chat.id,'2. В этом боте есть команды /learn, /help, /addword и /start ;')
    bot.send_message(message.chat.id,'3. Его автор великий професор наук Марк Грачёв.')

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
