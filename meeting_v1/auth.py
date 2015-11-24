#!/usr/bin/env python

from regist import User_reg

def Baseauth(username,password):
	res  = User_reg()
	result = res.Auth_dict()
	for user in result:
		if user == username:
			if result[user][1] == password:
				return 'auth ok'
				if result[user][0] == 'admin':
					import manager_api
				else:
					import custom_api
			else:
				return 'auth not ok'

print Baseauth('Tom',123456)
