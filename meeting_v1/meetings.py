#!/usr/bin/env python
# -*- coding: utf8 -*-
from dborm import *

class Meeting_manage(object):
	def __init__(self):
		self.Session = sessionmaker(bind=db)
		self.session = self.Session()
	def Add_meeting_to_db(self,title,content,leader,meeting_time):
		#发布会议接口，管理员控制
		every_meeting = Meeting(title=title,content=content,\
		leader=leader,meeting_time=meeting_time)
		self.session.add(every_meeting)
		self.session.commit()
		self.session.close()
	def Search_meeting_from_db(self):
		#会议查询接口
		self.search_dict = {}
		for s in self.session.query(Meeting).all():
			self.search_dict[s.meeting_id] = (s.title,s.content,s.leader,s.meeting_time)
		return self.search_dict
	def Del_meeting_from_db(self,ID):
		#删除过期会议接口，管理员控制
		self.session.query(Meeting).filter(Meeting.meeting_id==ID).delete()
		self.session.commit()
		self.session.close()
	def Update_meeting_to_db(self,title,chg_obj,chg_content):
		#修改会议内容接口，管理员控制
		self.session.query(Meeting).filter(Meeting.title==title).update({chg_obj:chg_content})
		
