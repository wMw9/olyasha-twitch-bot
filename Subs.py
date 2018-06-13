#from Settings import CLIENT_ID
from tkn import CLIENT_ID
import threading
import requests #import Request, urlopen
usr = []
sub = []

def addUsrfromchat(name, ts, mail, issub, sentmail, sentirc, other):
	usr.append({'name' : name, 'ts' : ts, 'mail' : mail, 'issub' : issub, 'sentmail' : sentmail, 'sentirc' : sentirc, 'other' : other})
	print(name + ' | ' + mail + ' | ' + 'added to usr list')
	print(usr)
	print(len(usr))

def checkUsrForSub():
	headers = {
	'Accept': 'application/vnd.twitchtv.v5+json',
	'Client-ID': CLIENT_ID,}
	r = requests.get('https://api.twitch.tv/kraken/users/41434114/chat/channels/104717035?api_version=5', headers=headers)
	return r.text


#
#print(checkUsrForSub())