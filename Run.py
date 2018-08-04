# -*- coding: utf-8 -*-
import string, time, threading, requests, os
from Initialize import joinRoom
#from Settings import INVITE
from tkn import INVITE, URL_TELE_API
from Subs import addUsrfromchat
from Read import getUser, getMessage, isSub, getId
from Socket import openSocket, sendMessage, sendWhisper
from Initialize import joinRoom

s = openSocket()
joinRoom(s)
s.send(bytes("CAP REQ :twitch.tv/tags" + "\r\n", 'UTF-8'))
s.send(bytes("CAP REQ :twitch.tv/commands" + "\r\n", 'UTF-8'))
s.send(bytes("CAP REQ :twitch.tv/membership" + "\r\n", 'UTF-8'))
readbuffer = ""
suicide = time.time() # Suicide timer

# PONG every 5 min
def pong():
    while True:
        time.sleep(300)
        s.send(bytes('PONG :tmi.twitch.tv\r\n', 'UTF-8'))
        print('sending pong')


t = threading.Thread(target=pong)
t.start()


# Check if we got D/C
def ping():
    while True:
        time.sleep(300)
        now = time.time()
        diff = now - suicide
        # print(diff)
        if diff > 350:
            print('Its been more than 300 seconds, restarting...')
            try:
                data_message = {'chat_id': 144149077, 'text': 'OlyashaTwitchBot отключился от чата, переподключаюсь...',
                                'disable_web_page_preview': True}
                r = requests.post(URL_TELE_API + 'sendMessage', data=data_message)
                print(r.text)
            except Exception as error:
                print('could not send telegram message' + error)
            os._exit(1)
        s.send(bytes('PING :tmi.twitch.tv\r\n', 'UTF-8'))
        print('Sending ping')


t2 = threading.Thread(target=ping)
t2.start()


while True:
        s_bytes = s.recv(1024)
        s_str = s_bytes.decode('utf-8')
        readbuffer = readbuffer + s_str #s.recv(1024)
        temp = readbuffer.split("\n")
        readbuffer = temp.pop()
        for line in temp:
            print(line)
            if "PONG tmi.twitch.tv" in line:
                # s.send(bytes('PONG :tmi.twitch.tv\r\n', 'UTF-8'))
                print('Got pong from twitch')
                suicide = time.time()
                break
            if "PING :tmi.twitch.tv" in line:
                s.send(bytes('PONG :tmi.twitch.tv\r\n', 'UTF-8'))
                break
            user = getUser(line)
            message = getMessage(line)
            if "!inv" in line:
                i = isSub(line)
                if i:
                    #print ('Да, он саб!')
                    sendWhisper(s, user, 'Привет, '+ user +'. Добро пожаловать в тайный чатик утиной армии, НИКОМУ не показывай ссылку!: ' + INVITE)
                    #addUsrfromchat(user, round(time.time()), '', True, 0, 0, '')
                    data_message = {'chat_id': 144149077, 'text': 'twitch.tv/' + user + ' запросил инвайт в ☆САБ ЧАТ★', 'disable_web_page_preview': True}
                    r_inst = requests.post(URL_TELE_API + 'sendMessage', data=data_message)
                    #getId(line)
                    break
                #print ('Не саб!!')
                #sendWhisper(s, user, 'Прости, ' + user + '... но ты не подписчик Оляши. Саб-чат в телеграме доступен только для солдатов утиной армии')
                break