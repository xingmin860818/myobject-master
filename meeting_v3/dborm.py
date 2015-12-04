#!/usr/bin/env python
# -*- coding:utf8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,and_,or_
from sqlalchemy import Column,Integer,String,ForeignKey,SMALLINT
from sqlalchemy.orm import sessionmaker,relationship,backref
import sqlalchemy
import config
from sqlalchemy.dialects.mssql import SMALLINT


Base = declarative_base()
#注册表类
class User_Regist(Base):
	__tablename__ = 'regist'

	id = Column(Integer,primary_key=True)
	#提示使用smallint，但没找到该类型
	ifdel = Column(SMALLINT,default=1)
	role = Column(String(10))
	user = Column(String(15),unique=True)
	password = Column(Integer)
	email = Column(String(40))

	#用于查询时获取所有信息
	def get_all(self):
		return{'id':self.id,'role':self.role,'user':self.user,'email':self.email}

#会议表类
class Meeting(Base):
	__tablename__ = 'meetings'
	
	id = Column(Integer,autoincrement=True,primary_key=True)
	ifdel = Column(SMALLINT,default=1)
	title = Column(String(100),unique=True)
	content = Column(String(1024))
	leader = Column(String(15))
	meeting_time = Column(String(20))

	def get_all(self):
		return{'id':self.id,'title':self.title,'content':self.content,'leader':self.leader,'time':self.meeting_time}
#报名表类
class User_Sign(Base):
	__tablename__ = 'sign'
	
	id = Column(Integer,primary_key=True)
	ifdel = Column(SMALLINT,default=1)
	title = Column(String(100),ForeignKey(Meeting.title))
	user = Column(String(15))

	def get_all(self):
		return{'id':self.id,'title':self.title,'user':self.user}
#评论表类
class User_Comment(Base):
	__tablename__ = 'comment'

	id = Column(Integer,primary_key=True)
	ifdel = Column(SMALLINT,default=1)
	user = Column(String(15))
	title = Column(String(100),ForeignKey(Meeting.title))
	user_comment = Column(String(1000))

	def get_all(self):
		return{'id':self.id,'user':self.user,'title':self.title,'comment':self.user_comment}



#定义数据库的增删改查操作
class Database(object):
	def __init__(self):
	#	db_conn = '{}://{}:{}@{}'.format(config.db_server,config.conn_user,config.password,config.conn_addr)
	#	db_server = 'use {}'.format(config.createdb)
		db_conn = 'mysql://recp:123456@192.168.20.237'
		db_server = 'use Meeting'
		db = create_engine(db_conn)
		db.execute(db_server)
		Base.metadata.create_all(db)
		Session = sessionmaker(bind=db)

		self.session = Session()
		
	def Add(self,table,**kwargs):
		try:
			keywards = table(**kwargs)
			self.session.add(keywards)
			self.session.commit()
			return True
		except (sqlalchemy.exc.IntegrityError,TypeError):
			self.session.rollback()
			raise
	#根据用户进行逻辑删除数据，隐藏特定字段值
	def Del_user(self,table,users):
		self.session.query(table).filter(table.user==users).update({'ifdel':'0'})
		self.session.commit()
		result = self.session.query(table).filter(table.ifdel==0,table.user==users).all()
		if result == []:
			return False
		else:
			return True
	#根据会议主题进行逻辑删除
	def Del_title(self,table,titles):
		self.session.query(table).filter(table.title==titles).update({'ifdel':'0'})
		self.session.commit()
		result = self.session.query(table).filter(table.ifdel==0,table.title==titles).all()
		if result == []:
			return False
		else:
			return True
	#更新数据库信息,匹配ID号，更改字段名的内容
	def Update(self,table,ID,chg_obj,chg_content):
		try:
			self.session.query(table).filter(table.id==ID).update({chg_obj:chg_content})
			self.session.commit()
			return True
		except sqlalchemy.exc.InvalidRequestError:
			self.session.rollback()
			raise
	def Search(self,table,val=None):
		reslist = []
		if val == None:
			pass
			for row in self.session.query(table).all():
				reslist.append(row.get_all())
			return reslist
		else:
			for line in self.session.query(table).filter(table.user==val).all():
				reslist.append(line.get_all())
			return reslist
	def Login_auth(self,auth_user):
		try:
			dic = {}
			res = self.session.query(User_Regist).filter(User_Regist.user==auth_user).one()
			dic[res.user]=(res.password,res.role)
			return dic
		except sqlalchemy.orm.exc.NoResultFound:
			return False
