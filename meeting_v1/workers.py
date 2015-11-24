#!/usr/bin/env python
#-*-coding:utf8-*-
'''用于人员控制，员工基类，管理员和普通员工继承基类，获得
基类的基本功能，管理员在基本功能之上具有会议修改权'''
import sqlalchemy
from dborm import *
from meetings import *
from sign_up import Sign_user
from comment import Com_plate
#from regist import User_registing
from regist import *
class Workers(object):
	'''基类具有管理员和普通员工共有的方法'''
	def __init__(self):
		#初始化接口实例
		self.meet = Meeting_manage()
		self.sign = Sign_user()
		self.com = Com_plate()
		self.regg = User_registing()
		self.result = self.Search_meet()
	def Search_meet(self):
		#从会议接口中查询会议
		result = self.meet.Search_meeting_from_db()
		return result
	def Look_patteners(self,meeting_title):
		#从用户接口中查询相同会议参会人
		users = self.sign.Show_meet_users(meeting_title)
		for title in users:
			if users[title] == []:
				return('no user or you input wrong title!')
			else:
				return users
	def Sign_up(self,meeting_title,user_name):
		#用户注册
		self.sign.Sign_up(meeting_title,user_name)
		result = self.sign.Show_meet_users(meeting_title)
		if result != {}:
			if user_name in result[meeting_title]:
				return('sign ok')
			else:
				return('sign fail')
	def Pub_com(self,username,meeting_title,user_comment):
		self.com.Public_com(username,meeting_title,user_comment)
		return('insert ok,you must check it later')
	def Search_comm(self,meetig_title):
		comm = self.com.Search_com()
		if comm == {}:
			return('no comment be found,no such title or wrong title')
		else:
			return comm
	def Regist(self,role,username,password):
		try:
			self.regg.Regist(role,username,password)
		except sqlalchemy.exc.IntegrityError:
			raise KeyError('this user has already registed')
	def Search_reg_user(self,username):
		print self.regg.Auth_dict()
		#return self.regg.Search_user(username)
class Managers(Workers):
	'''管理员拥有对会议的增删改功能'''
	def __init__(self):
		super(Managers,self).__init__()
	def Add_meetings(self,title,content,leader,meeting_time):
		#新增会议
		self.meet.Add_meeting_to_db(title,content,leader,meeting_time)
		title_value = [y[0] for x,y in self.result.iteritems()]
		if title in title_value:
			return('Add meeting ok')
		else:
			return('Add meeting not ok')
	def Del_meetings(self,ID):
		#通过会议id号删除过期会议
		self.meet.Del_meeting_from_db(ID)
		for ids in self.result:
			if ID == ids:
				return 'Delete failed'
			else:
				return 'Delete success'
	def Update_meeting(self,content,chg_obj,chg_content):
		#更改已发布会议内容
		self.meet.Update_meeting_to_db(content,chg_obj,chg_content)
	def Del_sign_user(self,ID):
		#对参会报名人员表进行人员管理
		self.sign.Del_user(ID)

class Customs(Workers):
	'''普通用户暂时不需要定制功能'''
	def __init__(self):
		super(Customs,self).__init__()


x = Managers()
#x.Regist('custom','bob','123456')
x.Search_reg_user('Tom')
