import Tkinter as tk

class Expense_Rec(object):
	""" Class defining Expense objects, which are
	used by the GUI"""

	def __init__(self, name, from_, to, current):
		"""Create a scale object."""
		self.name = name
		self.from_ = from_
		self.to = to
		self.current = current

	def set_current(self, new):
		"""Updates the current value of the expense"""
		self.current = current 






