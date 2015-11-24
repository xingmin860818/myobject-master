#!/usr/bin/env python
#-*-coding:utf8-*-
'''用于人员控制，员工基类，管理员和普通员工继承基类，获得
基类的基本功能，管理员在基本功能之上具有会议修改权'''
from dborm import *
class Person(object):
	'''基类具有管理员和普通员工共有的方法'''
	def __init__(self):
		#初始化接口实例
		self.database = Database()
	#查询会议，*args代表查询的字段
	def Search_meet(self,val=None):
		#从会议接口中查询会议
		result = self.database.Search(Meeting,val)
		return result
	#从用户接口中查询相同会议参会人
	def Look_patteners(self,ID):
		result = self.database.Search(sign,ID)
		return result
	#用户报名会议
	def Sign_up(self,**kwargs):
		return self.database.Add(User_Sign,**kwargs)
	#用户发表评论
	def Pub_com(self,**kwargs):
		return self.database.Add(User_Comment,**kwargs)
	#用户注册
	def Regist_user(self,**kwargs):
		return self.database.Add(User_Regist,**kwargs)
	def Search_comment(self,ID):
		return self.database.Search(User_comment,ID)
class Managers(Person):
	'''管理员拥有对会议的增删改功能'''
	def __init__(self):
		super(Managers,self).__init__()
	#新增会议
	def Add_meetings(self,**kwargs):
		return self.database.Add(Meeting,**kwargs)
	#删除会议
	def Del_meetings(self,ID):
		return self.database.Del(Meeting,ID)
	#更改已发布会议内容
	def Update_meeting(self,ID,chg_obj,chg_content):
		return self.database.Update(Meeting,ID,chg_obj,chg_content)
	#删除注册用户
	def Del_sign_user(self,ID):
		#对参会报名人员表进行人员管理
		return self.database.Del(User_Sign,ID)
	def Search_reg_user(self,ID):
		return self.database.Search(User_Regist,ID)
	def Del_reg_user(self,ID):
		return self.database.Del(User_Regist,ID)

class Customs(Person):
	'''普通用户暂时不需要定制功能'''
	def __init__(self):
		super(Customs,self).__init__()

