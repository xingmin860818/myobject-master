#!/usr/bin/env python
# -*- coding:utf8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship,backref

db_conn = 'mysql://root:123456@127.0.0.1'
db_server = 'use Meeting'
db = create_engine(db_conn)
db.execute(db_server)
Base = declarative_base()

'''定义三张表'''
#定义会议表
class User_regist(Base):
	__tablename__ = 'user'

	role = Column(String(10))
	user_name = Column(String(15),primary_key=True)
	password = Column(Integer)

class Meeting(Base):
	__tablename__ = 'meetings'
	
	meeting_id = Column(Integer,primary_key=True)
	title = Column(String(100))
	content = Column(String(1024))
	leader = Column(String(15))
	meeting_time = Column(String(20))

class User_sign(Base):
	__tablename__ = 'baomingbiao'

	user_id = Column(Integer,primary_key=True)
	meeting_title = Column(String(100),primary_key=True)
	user_name = Column(String(15))

class Comment_plateform(Base):
	__tablename__ = 'pinglun'

	id = Column(Integer,primary_key=True)
	user_name = Column(String(15))
	meeting_title = Column(String(100))
	user_comment = Column(String(1000))
Base.metadata.create_all(db)
#定义报名表参会


