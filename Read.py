import string

def getUser(line):
	#print(line)
	separate = line.split(":", 2)
	#print ('getUser: ')
	#print (separate)
	#print ('getUser (separate[1]: ')
	#print (separate[1])
	user = separate[1].split("!", 1)[0]
	print (user)
	return user
def getMessage(line):
	#print(line)
	#separate = line.split(":", 2)
	separate = line.split(":", 2)
	#print ('getMessage: ')
	print(len(separate))
	#print(separate)
	if len(separate) == 3:
		message = separate[2]
		#print (separate[2])
	else:
		message = separate[1]
		#print (separate[1])
	#print (separate[0])
	#print (separate[1])
	#print (separate[2])
	#message = separate[2]
	#print (message)
	return message

def isSub(line):
	separate = line.split(":", 2)
	print(len(separate))
	print(separate)
	if len(separate) == 3:
		message = separate[0]
	else:
		message = separate[0]
	return message