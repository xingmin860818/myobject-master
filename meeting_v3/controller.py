from dborm import *
from view import View

class Controller(object):
	def __init__(self):
		self.data = Database()
		self.viewer = View()
	def get_table_info(self,table):
		task = self.data.Search(table)
		return self.viewer.get_task(task)

c = Controller()
print c.get_table_info(Meeting)
