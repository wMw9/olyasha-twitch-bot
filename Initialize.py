import string
from Socket import sendMessage, sendWhisper
def joinRoom(s):
	readbuffer = ""
	Loading = True
	while Loading:
		print ('Initialize.py: Loading cycle')
		s_bytes = s.recv(1024)
		s_str = s_bytes.decode('utf-8')
		readbuffer = readbuffer + s_str #s.recv(1024)
		#readbuffer = readbuffer + s.recv(1024)
		#temp = string.split(readbuffer, "\n")
		temp = readbuffer.split("\n")
		#print('Initialize.py: print temp.pop(): ' + temp.pop(0))
		readbuffer = temp.pop()
		
		for line in temp:
			print(line)
			Loading = loadingComplete(line)
	#sendMessage(s, "Successfully joined chat")
	sendWhisper(s, "wmw_", "Successfully joined chat")
	#sendMessage(s, "CAP REQ :twitch.tv/tags")
	#s.send(bytes("CAP REQ :twitch.tv/tags" + "\r\n", 'UTF-8'))
	#s.send(bytes("CAP REQ :twitch.tv/commands" + "\r\n", 'UTF-8'))
	
def loadingComplete(line):
	if("End of /NAMES list" in line):
		#print('loadingComplete() set False')
		#s.send(bytes("CAP REQ :twitch.tv/tags" + "\r\n", 'UTF-8'))
		#s.send(bytes("CAP REQ :twitch.tv/commands" + "\r\n", 'UTF-8'))
		return False
	else:
		print('loadingComplete() set True')
		return True