from ExpenseRec import ExpenseRec
import random
import string
import csv


class Budget(object):
	"""Class for calculating my budget based on fixed and variable costs, which 
	can be set from the GUI class
	"""

	field_names = ['id_', 'name', 'from_', 'to', 'current', 'deleted']


	def __init__(self, savings, save_file = None):
		""" Initializes the budget program with the amount in savings.
		Creates an empty expense_rec list, which represents the list of 
		recurring expenses.
		"""
		self.savings = savings
		self.save_file = save_file
		self.expenses_rec = self.get_saved_expenses_rec()

	def get_saved_expenses_rec(self):
		""" 
		"""
		if self.save_file is None:
			self.save_file = ''.join(random.choice(string.ascii_uppercase 
							+ string.ascii_lowercase + string.digits) 
							for _ in range(16)) + '.csv'
			with open(self.save_file, 'w+') as save_file:
				csv.DictWriter(save_file, Budget.field_names).writeheader()
			print self.save_file
			return []
		else:
			"""TO ADD: read file from CSV
			Create an expense object for each non-deleted line in the CSV.
			Return a list of expense objects."""
			return []

	def create_expense_rec(self, id_, name, from_, to, start_val):
		"""Adds an ExpenseRec object to the expenses_rec list.
		"""
		new = ExpenseRec(id_, name, from_, to, start_val)
		self.expenses_rec.append(new)
		self.add_expense_to_file(new)

	def add_expense_to_file(self, new):
		with open(self.save_file, 'a') as save_file:
			csv.DictWriter(save_file, fieldnames = Budget.field_names).writerow(
				{'id_' : new.id_,
				'name' : new.name,
				'from_': new.from_,
				'to' : new.to,
				'current': new.current,
				'deleted': new.deleted})

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
		return self.savings / self.get_burndown_rate()

	def save(self):
		#print "foo"
		pass 




