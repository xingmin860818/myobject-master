#!/usr/bin/env python
# -*- coding: utf8 -*-
'''管理员接口'''
from workers import Managers
from dborm import *
man = Managers()
def Add_meeting(title,content,leader,meeting_time):
	return man.Addmeetings(title,content,leader,meeting_time)

def Del_meeting(ID):
	return man.Del_meetings(ID)

def Up_meeting(content,chg_obj,chg_content):
	return man.Update_meeting(content,chg_obj,chg_content)

def Del_sign_user(ID):
	return man.Del_user(ID)

def Search_meetings():
	return man.Search_meet()

def Look_patteners(meeting_title):
	return man.Look_patteners(meeting_title)

def Sign_up(meeting_title,user_name):
	return man.Sign_up(meeting_title,user_name)

def Pub_pinglun(username,meeting_title,user_comment):
	return man.Pub_com(username,meeting_title,user_comment)

def Search_pinglun(meeting_title):
	return man.Search(meeting_title)

def Regist(role,username,password):
	return man.Regist(role,username,password)

def Search_reg_user(username):
	return man.Search_reg_user(username)

def Del_reg_user(username):
	return man.Del_reg_user(username)

Regist('custom','jerry','123456')
Regist('custom','lucy','123456')
