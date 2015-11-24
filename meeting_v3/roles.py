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
	#更改已发布会议内容
	def Update_meeting(self,ID,chg_obj,chg_content):
		return self.database.Update(Meeting,ID,chg_obj,chg_content)
	#查看注册用户
	def Search_reg_user(self,ID):
		return self.database.Search(User_Regist,ID)
	#删除会议
	def Del_meetings(self,titles):
		self.database.Del_title(User_Sign,titles)
		self.database.Del_title(User_Comment,titles)
		res = self.database.Del_title(Meeting,titles)
		if res == False:
			raise NameError('no {} be found'.format(titles))
		else:
			return True
	#删除注册用户
	def Del_reg_user(self,users):
		self.database.Del_user(User_Sign,users)
		self.database.Del_user(User_Comment,users)
		res = self.database.Del_user(User_Regist,users)
		if res == False:
			raise NameError('no {} be found'.format(users))
		else:
			return True
	#对参会报名人员表进行人员管理
	def Del_sign_user(self,users):
		return self.database.Del_user(User_Sign,users)
	#删除用户评论信息
	def Del_comment(self,users):
		return self.database.Del_user(User_Comment,users)

class Customs(Person):
	'''普通用户暂时不需要定制功能'''
	def __init__(self):
		super(Customs,self).__init__()
