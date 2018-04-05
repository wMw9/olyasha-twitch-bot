import socket
from Settings import HOST, PORT, PASS, IDENT, CHANNEL

def openSocket():
	
	s = socket.socket()
	s.connect((HOST, PORT))
	s.send(bytes("PASS " + PASS + "\r\n", 'UTF-8'))
	s.send(bytes("NICK " + IDENT + "\r\n", 'UTF-8'))
	s.send(bytes("JOIN #" + CHANNEL + "\r\n", 'UTF-8'))
	#s.send(bytes("CAP REQ :twitch.tv/tags" + "\r\n", 'UTF-8'))
	#s.send(bytes("CAP REQ :twitch.tv/commands" + "\r\n", 'UTF-8'))
	return s
	
def sendMessage(s, message):
	messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
	#s.send(messageTemp + "\r\n")
	s.send(bytes(messageTemp + "\r\n", 'UTF-8'))
	print("Sent: " + messageTemp)

def sendWhisper(s, user, message):
	messageTemp = "PRIVMSG #" + CHANNEL + " :/w " + user + " " + message
	#s.send("PRIVMSG #wmw_ :/w " + username + " " + message + "\r\n")
	#s.send(messageTemp + "\r\n")
	s.send(bytes(messageTemp + "\r\n", 'UTF-8'))
	print("Sent: " + messageTemp)