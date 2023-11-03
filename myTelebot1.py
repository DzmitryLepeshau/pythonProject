import telebot
import random

API_TOKEN = "6732055091:AAFeVPrbKIoYUlsEBb3vXPYUTA7U6zjw5Gk"

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     'Hello player!')
    keyboard = telebot.types.ReplyKeyboardMarkup()
    red_button = telebot.types.KeyboardButton('🟥')
    black_button = telebot.types.KeyboardButton('⬛️')
    keyboard.add(red_button)
    keyboard.add(black_button)
    bot.send_message(message.chat.id,
                     'Guess the colour 🟥 or ⬛️',
                     reply_markup=keyboard)

    bot.register_next_step_handler(message, answer_card)


def answer_card(message):
    value, suit = generate_random_card()
    player_answer = message.text
    if player_answer == '🟥' and suit in ['H', 'D']:
        bot.send_message(message.chat.id,
                         f'Correct! The card was: {value}{suit}')
    elif player_answer == '⬛️' and suit in ['C', 'S']:
        bot.send_message(message.chat.id,
                         f'Correct! The card was: {value}{suit}')
    else:
        bot.send_message(message.chat.id,
                         f'Incorrect! The card was: {value}{suit}')

    start(message)
def generate_random_card():
    value = random.choice(
        ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"])
    suit = random.choice(["H", "D", "C", "S"])
    return value, suit


bot.infinity_polling()
