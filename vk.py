#easy_install pip
#python get-pip.py
#pip install vk_api

import vk_api #импортируем библиотеки для работы
import time
import random
tok = os.environ.get('bot_token')
vk_session = vk_api.VkApi(token = 'eefe30e0d24a4824f03400c50d82b21899c954cc4b0d7b8e5e2815ccbe242387fb97825d48b931b811f04')    # создаем ссесси для работы и подключаем апи

from vk_api.longpoll import VkEventType, VkLongPoll                  # импортируем нужные библиотеки модуля вк апи
longpoll = VkLongPoll(vk_session)                                     # созаем переменную и в нее
                                                                      # передаем нашу сессию соединения

vk= vk_session.get_api()                                             # получим вк api

global Random
def random_id():
    Random = 0
    Random+=random.randint(0,10000000)
    return  Random

#  в бесконечном цикле будем проверять входящие эвенты
while True:
    for event in longpoll.listen():                                   # заставим слушать входящие эвенты и проверяем каждый входящий эвент
          if event.type ==VkEventType.MESSAGE_NEW and event.to_me:    # если тип эвента новое сообщение, и сообщение боту то
              if event.text.lower() == "привет":                      #проверяем наш эвент в нижнем регистре
                 vk.messages.send(                                    # event.user_id юзер который написал, и сообщение для ответа
                     user_id = event.user_id,
                     message = "привет, человек",
                   #  keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                     random_id = random_id()                          #random_id случайное сообщение, чтобы бот не присылол одно и тоже сообщение неколько раз
                 )
              elif event.text.lower() == "как дела?":                      #проверяем наш эвент в нижнем регистре
                 vk.messages.send(                                    # event.user_id юзер который написал, и сообщение для ответа
                     user_id = event.user_id,
                     message = "как у робота",
                     keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                     random_id = random_id()                          #random_id случайное сообщение, чтобы бот не присылол одно и тоже сообщение неколько раз
                 )
              elif event.text.lower() == "как дела":  # проверяем наш эвент в нижнем регистре
                 vk.messages.send(  # event.user_id юзер который написал, и сообщение для ответа
                     user_id=event.user_id,
                     message="как у робота",
                     random_id=random_id()
                     # random_id случайное сообщение, чтобы бот не присылол одно и тоже сообщение неколько раз
                 )
              elif event.text.lower() == "Сколько лет?":  # проверяем наш эвент в нижнем регистре
                  vk.messages.send(  # event.user_id юзер который написал, и сообщение для ответа
                      user_id=event.user_id,
                      message="Я совсем молодой",
                      keyboard=open("key.json", "r", encoding="UTF-8").read(),
                      random_id=random_id()
                      # random_id случайное сообщение, чтобы бот не присылол одно и тоже сообщение неколько раз
                  )
              elif event.text.lower() == "Зачем я?":      # проверяем наш эвент в нижнем регистре
                 vk.messages.send(  # event.user_id юзер который написал, и сообщение для ответа
                     user_id=event.user_id,
                     message="как у робота",
                     keyboard=open("keyboard.json", "r", encoding="UTF-8").read(), # подгружаем json
                     random_id=random_id()
                     # random_id случайное сообщение, чтобы бот не присылол одно и тоже сообщение неколько раз
                 )

              else:
                  vk.messages.send(  # event.user_id юзер который написал, и сообщение для ответа
                      user_id=event.user_id,
                      message="я тебя не понимаю",
                      random_id=random_id()
                      # random_id случайное сообщение, чтобы бот не присылол одно и тоже сообщение неколько раз
                  )

'''
Создаем новый файл с расширением json - файл для обмена данными на js

{
  "one_time": false,  - переменная, которая отвечает за закрытие клавиатуры при написании сообщения, если false - окно висит
  "buttons": [ описываем массив из кнопок
    [ 
      {
        "action": { 
          "type": "text", - тип кнопки
          "label": "привет" - название кнопки и текст, который она отправляет
        },
        "color": "positive"  - зеленый  \ "negative" - красный(внимание) "primary" - синий "secondary" - белый 
     }
      {
        "action": {
          "type": "text",
          "label": "как дела?"
        },
        "color": "positive"
      }
    ]
дополнительные данные можно найти здесь
'''
