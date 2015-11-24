#!/usr/bin/env python
# -*- coding: utf8 -*-
'''管理员接口'''
from workers import Customs
cus = Customs()
def Search_meetings():
	return cus.Search_meet()

def Look_patteners(meeting_title):
	return cus.Look_patteners(meeting_title)

def Sign_up(meeting_title,user_name):
	return cus.Sign_up(meeting_title,user_name)

def Pub_pinglun(username,meeting_title,user_comment):
	return cus.Pub_com(username,meeting_title,user_comment)

def Search_pinglun(meeting_title):
	return cus.Search(meeting_title)

print Search_meetings()
