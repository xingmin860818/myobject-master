#!/usr/bin/env python
# -*- coding: utf8 -*-
'''员工会议评论平台，发表参会后的感想'''
from dborm import *

class Com_plate(object):
	def __init__(self):
		self.Session = sessionmaker(bind=db)
		self.session = self.Session()
	def Public_com(self,user_name,meeting_title,user_comment):
		every_com = Comment_plateform(user_name=user_name,meeting_title=meeting_title,user_comment=user_comment)
		self.session.add(every_com)
		self.session.commit()
		self.session.close()
	def Search_com(self):
		self.search_com = {}
		for s in self.session.query(Comment_plateform).all():
			self.search_com[s.id] = (s.user_name,s.meeting_title,s.user_comment)
		return self.search_com
	def Del_com(self,user_name):
		self.session.query(Comment_plateform).filter(Comment_plateform.user_name==user_name).delete()
		self.session.commit()
		self.session.close()

