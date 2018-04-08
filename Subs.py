# -*- coding: utf-8 -*-
import requests, time
from Settings import CLIENT_ID

usr = []
sub = []

def addUsr(userid, name, issub, mail, ts):
	usr.append({'userid': userid, 'name' : name, 'issub' : issub, 'mail' : mail, 'ts' : ts})
	print (len(usr))
	print (usr)

addUsr(1234, 'wmw', True, 'wmw@mail.ru', round(time.time()))
addUsr(1234, 'wmw', True, 'wmw@mail.ru', round(time.time()))