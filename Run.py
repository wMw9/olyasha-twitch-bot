import string
from Read import getUser, getMessage, isSub
from Socket import openSocket, sendMessage, sendWhisper
from Initialize import joinRoom
from Settings import INVITE

s = openSocket()
joinRoom(s)
s.send(bytes("CAP REQ :twitch.tv/tags" + "\r\n", 'UTF-8'))
#s.send(bytes("CAP REQ :twitch.tv/commands" + "\r\n", 'UTF-8'))
readbuffer = ""

while True:
		print ('Run.py cycle')
		s_bytes = s.recv(1024)
		s_str = s_bytes.decode('utf-8')
		readbuffer = readbuffer + s_str #s.recv(1024)
		#temp = string.split(readbuffer, "\n")
		#print(readbuffer)
		#print ('Run.py cycle')
		temp = readbuffer.split("\n")
		readbuffer = temp.pop()
		#print (temp)
		#print (readbuffer)
		for line in temp:
			print(line)
			if "PING :tmi.twitch.tv" in line:
				s.send(bytes('PONG :tmi.twitch.tv\r\n', 'UTF-8'))
				break
			user = getUser(line)		
			#print (getMessage(line))
			message = getMessage(line)
			#print ('message: ' + message)
			print (user + ": " + message)
			if "!inv" in message:
				i = isSub(line)
				if ("subscriber=1" in i) or ("@badges=moderator" in i) or ("@badges=broadcaster" in i):
					#print ('Да, он саб!')
					sendWhisper(s, user, 'пукПривет, '+ user +'. Добро пожаловать в тайный чатик утиной армию, НИКОМУ не показывай ссылку!: ' + INVITE)
					break
				#print ('Не саб!')
				sendWhisper(s, user, 'Прости, ' + user + '... но ты не подписчик Оляши. Саб-чат в телеграме доступен только для солдатов утиной армии')
				break
			#if "suck" in message:
			#	sendMessage(s, "No, you suck!")
			#	break