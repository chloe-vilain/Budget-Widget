import Tkinter as tk

class ExpenseRec(object):
	""" Class defining ExpenseRec objects, which represents a 
		recurring expense. """

	def __init__(self, name, from_, to, current):
		"""Create an ExpenseRec object. Attributes include: name, the expense label (str);
		from_, the min value (int); to, the max value (int); current, the value
		currently set (str) """
		self.name = name
		self.from_ = from_
		self.to = to
		self.current = current

	def set_current(self, new):
		"""Updates the current value of the expense"""
		self.current = new 






