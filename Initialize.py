import string
from Socket import sendMessage, sendWhisper
def joinRoom(s):
	readbuffer = ""
	Loading = True
	while Loading:
		s_bytes = s.recv(1024)
		s_str = s_bytes.decode('utf-8')
		readbuffer = readbuffer + s_str #s.recv(1024)
		temp = readbuffer.split("\n")
		readbuffer = temp.pop()
		
		for line in temp:
			print(line)
			Loading = loadingComplete(line)
	#sendWhisper(s, "wmw_", "Successfully joined chat")
	
def loadingComplete(line):
	if("End of /NAMES list" in line):
		return False
	else:
		return True