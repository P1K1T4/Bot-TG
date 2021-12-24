import telebot
from telebot import types
import random

token = "5061324735:AAFN8TldjPkCY_wRV5Qq835IlRkvv6oSexU"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row('/help')
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом, хочешь расскажу, что я умею?".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html',reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def printer(message):
    salam = types.ReplyKeyboardMarkup()
    salam.row('Рандомное число', '/privet', '/MTUCI', '/help')
    bot.send_message(message.chat.id,
                                    'Ну, давай подскажу тебе, что я умею, смотри:'
                                    'Я могу написать тебе рандомное число(просто напиши Рандомное число)' 
                                    'Могу спросить, как у тебя дела(напиши /privet)' 
                                    'Могу рассказать тебе про МТУСИ(/MTUCI)', reply_markup=salam)


@bot.message_handler(commands=['MTUCI'])
def MTUCI(message):
    aboba = types.ReplyKeyboardMarkup()
    aboba.row('История МТУСИ', 'Где он находится?', 'Мнение о педагогическом составе', '/help')
    bot.send_message(message.chat.id, 'Вижу,ты заинтересован в МТУСИ, поэтому выбери то, что тебе интересно', reply_markup=aboba)


@bot.message_handler(commands=['privet'])
def zdarova(message):
    hello = types.ReplyKeyboardMarkup()
    hello.row("Как у тебя дела?", "Нормально", 'Плохо', 'Не очень', 'Все круто', '/help')
    bot.send_message(message.chat.id, 'Штош, давай поболтаем', reply_markup=hello)
    

@bot.message_handler(content_types=['text'])
def balda(message):
    if message.text == 'История МТУСИ':
        bot.send_message(message.chat.id, 'Московский технический университет связи и информатики (сокр. МТУСИ) — российский отраслевой университет в области информационных технологий, телекоммуникаций, информационной безопасности. 1918 — Издание Ленинского декрета о централизации радиотехнического дела Советской республики. Февраль 1919 — В дополнение к существовавшей телеграфной школе в Москве создана радиошкола, в этом же году обе школы объединяются в одно учебное заведение.')
    if message.text == 'Где он находится?':
        bot.send_message(message.chat.id, 'Он находится по адресу: Авиамоторная ул., 8А, Москва ')
    if message.text == 'Мнение о педагогическом составе':
        bot.send_message(message.chat.id, 'Я считаю, что в данном университете работают хорошие преподаватели, они знают свой предмет и поэтому обучают ему очень хорошо')
    if message.text == 'Как у тебя дела?':
        bot.send_message(message.chat.id, 'У меня все хорошо, правда, я машина, но спасибо конечно, а у тебя как?')
    if message.text == 'Нормально':
        bot.send_message(message.chat.id, 'Хорошо, я рад за тебя')
    if message.text == 'Рандомное число':
        bot.send_message(message.chat.id, str(random.randint(0, 10000)))
    if message.text == 'Плохо':
        bot.send_message(message.chat.id, 'Блин, ну ты не расстраивайся, все будет хорошо.')
    if message.text == 'Все круто':
        bot.send_message(message.chat.id, 'Хорошо, я рад за тебя')
    if message.text == 'Не очень':
        bot.send_message(message.chat.id, 'Блин, ну ты не расстраивайся, все будет хорошо.')

#@bot.message_handler(content_types=['text'])
#def lalala(message):
    #if message.text == 'Рандомное число':
        #bot.send_message(message.chat.id, str(random.randint(0, 1000)))
#@bot.message_handler(commands=['support'])
#def start_message(message):
    #bot.send_message(message.chat.id, 'Well, lets speak with our support')


#@bot.message_handler(commands=['info'])
#def start_message(message):
    #bot.send_message(message.chat.id, 'Would you like me to tell you about our University?')



#@bot.message_handler(content_types=['text'])
#def answer(message):
    #bot.send_message(message.chat.id, message.text)


#@bot.message_handler(commands=['aboba'])
#def answer(message):
    #bot.send_message(message.chat.id, ' Ну давай, нападай')
    #if message.text.lower() == 'да':
        #bot.send_message(message.chat.id, 'Нет')
    #if message.text.lower() == "нет":
        #bot.send_message(message.chat.id, 'Да')


#@bot.message_handler(commands=['Yes'])
#def answer(message):
    #if message.text.lower() == "I want it":
        #return
    #bot.send_message(message.chat.id, 'Well, touch the following link – https://mtuci.ru/')


#@bot.message_handler(content_types=['Yes'])
#def answer(message):
    #if message.text.lower() == 'Yes':
        #return
    #bot.send_message(message.chat.id, 'Well, touch the following link – https://mtuci.ru/')
    #if message.text.lower() == 'No':
        #return
    #bot.send_message(message.chat.id, 'Ok, see you when you would like it')



# RUN
bot.polling(none_stop=True)