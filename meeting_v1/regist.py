#!/usr/bin/env python
#-*-coding:utf8-*-
from dborm import *

class User_registing(object):
	def __init__(self):
		self.Session = sessionmaker(bind=db)
		self.session = self.Session()
		self.auth_dic = {}
	def Regist(self,role,username,password):
		every_regist = User_regist(role=role,user_name=username,password=password)
		self.session.add(every_regist)
		self.session.commit()
		self.session.close()
	def Search_user(self,username):
		self.result = self.session.query(User_regist.user_name).filter(User_regist.user_name==username)
		self.lis = []
		for name in self.result:
			self.lis.append(name)
		return self.lis
	def Auth_dict(self):
		for s in self.session.query(User_regist).all():
			self.auth_dic[s.user_name] = (s.role,s.password)
		return self.auth_dic
	def Del_regist_user(self,username):
		self.session.query(User_regist).filter(User_regist.user_name==username).delete()
		self.session.commit()
		self.session.close()

