from ExpenseRec import ExpenseRec

import csv


class Budget(object):
	"""Class for calculating my budget based on fixed and variable costs, which 
	can be set from the GUI class
	"""


	def __init__(self, savings): 
		""" Initializes the budget program with the amount in savings.
		Creates an empty expense_rec list, which represents the list of 
		recurring expenses.
		"""
		self.savings = savings
		self.expenses_rec = []

	def create_expense_rec(self, id_, name, from_, to, start_val):
		"""Adds an ExpenseRec object to the expenses_rec list.
		"""
		new = ExpenseRec(id_, name, from_, to, start_val)
		self.expenses_rec.append(new)

	def get_burndown_rate(self):
		""" Returns the monthly burn-down rate based on all known costs
		"""
		start = 0 
		for expense_rec in self.expenses_rec:
			start = start + int(expense_rec.current)
		return start

	def get_months_remaining(self):
		"""Returns the total months remaining based on the start savings
		and the monthly burn-down rate. 
		"""
		try:
			return self.savings / self.get_burndown_rate()
		except ZeroDivisionError:
			return 'N/A'  






