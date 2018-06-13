#import string
from Subs import addUsrfromchat
import re

def getId(line):
	separate = line.split(':')
	match = re.search(';user-id=(.*);user-type=', separate[0])
	print (match.group(1))
	return match.group(1)

def getUser(line):
	separate = line.split(":", 2)
	user = separate[1].split("!", 1)[0]
	return user
def getMessage(line):
	separate = line.split(':')
	if len(separate) == 3:
		message = separate[2]
	else:
		message = separate[1]
	return message

def getUserId(line):
	separate = line.split(':')
	#userid = separate

def isSub(line):
	s = line.split(":")
	if ("subscriber=1" in s[0]) or ("@badges=moderator" in s[0]) or ("@badges=broadcaster" in s[0]):
		#addUsrfromchat(name, ts, mail, issub, sentmail, sentirc, other)
		return True
	else:
		return False