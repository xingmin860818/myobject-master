#!/usr/bin/env python
import unittest
from manager_api import *

class Test_meeting(unittest.TestCase):
	def test_db_control(self):
		add = Add_meeting(title='ddhg',content='b',leader='c',meeting_time='d')
		update = Update_meeting(1,'title','x')
		del_meeitng = Del_meeting(1)
		searchall = Search_meetings()
		self.assertEquals(add,True)
		self.assertEquals(update,True)
		self.assertEquals(del_meeting,True)
		self.assertTrue(isinstance(searchall,dict))
	def testerror(self):
		with self.assertRaises(TypeError):
			Add_meeting('abd','e','f','g')
		Add_meeting(title='ddhg',content='b',leader='c',meeting_time='d')
		with self.assertRaises(sqlalchemy.exc.IntegrityError):
			Add_meeting(title='ddh',content='c',leader='d',meeting_time='f')
		with self.assertRaises(sqlalchemy.exc.InvalidRequestError):
			Update_meeting(99,'title','x')
		with self.assertRaises(orm_exc.NoResultFound):
			Look_patteners('x')
if __name__ == '__main__':
	unittest.main()
