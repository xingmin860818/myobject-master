#!/usr/bin/env python
# -*- coding: utf8 -*-
'''定义用户报名类'''
from dborm import *

class Sign_user(object):
	def __init__(self):
		self.Session = sessionmaker(bind=db)
		self.session = self.Session()
	def Sign_up(self,meeting_title,user_name):
		#用户注册接口，向数据库插入注册信息
		every_user = User_sign(meeting_title=meeting_title,user_name=user_name)
		self.session.add(every_user)
		self.session.commit()
		self.session.close()
	def Show_meet_users(self,meeting_title):
		#查询相同会议参会人员接口
		lis = []
		self.sign_users = {}
		self.users = self.session.query(User_sign.user_name).filter_by(meeting_title=meeting_title)
		for usr in self.users:
			if usr == '':
				return ValueError("there is no title:%s" % meeting_title)
			else:
				lis.append(usr[0])
		self.sign_users[meeting_title] = lis
		return self.sign_users
	def Del_user(self,ID):
		#删除报名人，由管理员控制
		self.session.query(User_sign).filter(User_sign.user_id==ID).delete()
		self.session.commit()
		self.session.close()
