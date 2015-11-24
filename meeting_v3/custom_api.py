#!/usr/bin/env python
# -*- coding: utf8 -*-
'''管理员接口'''
from roles import Customs
from auth import LoginForm

cus = Customs()
logger = LoginForm()

def Login(name,passwd):
	return logger.Login(name,passwd)

def Regist(name,passwd,email=None,role='Custom',**kw):
	return logger.Regist(name,passwd,email,role,**kw)

def Search_meetings(ID):
	return cus.Search_meet(ID)

def Look_patteners(ID):
	return cus.Look_patteners(ID)

def Sign_up(**kwargs):
	return cus.Sign_up(**kwargs)

def Pub_comment(**kwargs):
	return cus.Pub_com(**kwargs)

def Search_comment(ID):
	return cus.Search_comment(ID)

