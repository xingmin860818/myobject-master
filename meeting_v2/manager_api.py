#!/usr/bin/env python
# -*- coding: utf8 -*-
from roles import Managers
from dborm import *
man = Managers()
def Add_meeting(**kwargs):
	return  man.Add_meetings(**kwargs)
def Del_meeting(ID):
	return man.Del_meetings(ID)

def Update_meeting(ID,chg_obj,chg_content):
	return man.Update_meeting(ID,chg_obj,chg_content)

def Del_sign_user(ID):
	return man.Del_user(ID)

def Search_meetings(val=None):
	return man.Search_meet()

def Look_patteners(val=None):
	return man.Look_patteners(val)

def Sign_up(**kwargs):
	return man.Sign_up(**kwargs)

def Pub_comment(**kwargs):
	return man.Pub_com(**kwargs)

def Search_comment(val=None):
	return man.Search(val=None)

#def Regist(**kwargs):
#	return man.Regist_user(**kwargs)

def Search_regist_user(val=None):
	return man.Search_reg_user(val)

def Del_reg_user(ID):
	return man.Del_reg_user(ID)

