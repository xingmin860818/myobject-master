#!/usr/bin/env python

<<<<<<< HEAD
from dborm import *
class Login_view(object):
	def Log_check(self,auth_dic,name,passwd):
		if auth_dic:
			for nm,pasd in auth_dic.iteritems():
				if nm == name and pasd[0] == passwd:
					return('check ok, you are a {}'.format(pasd[1]))
				else:
					return('login fail')
		else:
			return('login fail')
class LoginForm(object):
	def __init__(self):
		self.database = Database()
		self.logview = Login_view()
	def Login(self,name,passwd):
		res = self.database.Login_auth(name)
		return self.logview.Log_check(res,name,passwd)
	def Regist(self,name,passwd,email=None,role='Custom',**kw):
			return self.database.Add(User_Regist,role=role,user=name,password=passwd,email=email)


