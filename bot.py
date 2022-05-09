# импорт всех необходимых модулей для работы
import telebot
import pyqrcode
import time
from telebot import types


token="5141580745:AAGxqQIgbx1G9B1ImObaqJXoSIim_pnT_bw" # токен для доступа к боту
mybot=telebot.TeleBot(token) # создаём нашего бота и подключаем токен


@mybot.message_handler(commands=['start'])
def welcome(message): # создаём функцию приветствия при первом запуске
    #клавиатура
    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # создаём клавиатуру
    item1 = types.KeyboardButton('🔑Получить QR-code') # создаём кнопку 

    keyboard_markup.add(item1) # добавляем кнопку на клавиатуру

    mybot.send_message(message.chat.id, 'Привет!\nМеня зовут <b>{1.first_name}</b>, и я умею делать QR-код по твоей ссылке!\nДля этого нажми на «🔑Получить QR-code»'.format(message.from_user, mybot.get_me()),
        parse_mode='html', reply_markup=keyboard_markup) # отсылаем приветственное сообщение пользователю


@mybot.message_handler(content_types=['text'])
def link(message):  # создаём функцию обработки кнопки и ссылки
    if message.chat.type == 'private': # даём боту понять, что ловить текст нужно в личных сообщениях
        if message.text == '🔑Получить QR-code': # условие для основной кнопки
            mybot.send_chat_action(message.chat.id, 'typing')
            msg = mybot.send_message(message.chat.id, '🔗Пришли мне свою ссылку, на которую нужно сделать QR-код') # присылаем пользователю сообщение, чтобы он отправил нам ссылку
            mybot.register_next_step_handler(msg, result) # функция, принимающая в аргументы сообщение (ссылку), а затем функцию, которая обработает сообщение
        else:
            mybot.send_message(message.chat.id, 'Я не знаю как на такое отвечать🥺') # если написать ему какой-либо текст, а не нажать на кнопку

def result(message):  # создаём функцию результата и отправки qr-кода
    url=pyqrcode.create(message.text)
    url.png('qrcode.png',scale=20) # задаём размер для png-картинок
    mybot.send_chat_action(message.chat.id, 'upload_document') # даём боту понять, что нужно делать с картинкой
    mybot.send_document(message.chat.id,open('qrcode.png','rb' )) # отправляем картинку пользователю





mybot.polling(non_stop=True) #команда для постоянной работы бота