#import string

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

def isSub(line):
	s = line.split(":")
	if ("subscriber=1" in s[0]) or ("@badges=moderator" in s[0]) or ("@badges=broadcaster" in s[0]):
		return True
	else:
		return False