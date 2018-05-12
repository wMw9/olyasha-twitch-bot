# -*- coding: utf-8 -*-
import string, requests
from Read import getUser, getMessage, isSub, getId
from Socket import openSocket, sendMessage, sendWhisper
from Initialize import joinRoom
from Settings import INVITE, URL_TELE_API

s = openSocket()
joinRoom(s)
s.send(bytes("CAP REQ :twitch.tv/tags" + "\r\n", 'UTF-8'))
s.send(bytes("CAP REQ :twitch.tv/commands" + "\r\n", 'UTF-8'))
s.send(bytes("CAP REQ :twitch.tv/membership" + "\r\n", 'UTF-8'))
readbuffer = ""

while True:
		s_bytes = s.recv(1024)
		s_str = s_bytes.decode('utf-8')
		readbuffer = readbuffer + s_str #s.recv(1024)
		temp = readbuffer.split("\n")
		readbuffer = temp.pop()
		for line in temp:
			print(line)
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

					data_message = {'chat_id': 144149077, 'text': 'twitch.tv/' + user + ' запросил инвайт в саб-чат', 'disable_web_page_preview': True}
					r_inst = requests.post(URL_TELE_API + 'sendMessage', data=data_message)
					#getId(line)
					break
				#print ('Не саб!')
				#sendWhisper(s, user, 'Прости, ' + user + '... но ты не подписчик Оляши. Саб-чат в телеграме доступен только для солдатов утиной армии')
				break