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
		self.expenses_rec = []
		self.get_saved_expenses_rec()

	def get_saved_expenses_rec(self):
		""" If save file exists, creates an expense for each entry in the file.
		If it does not exist, create a new save file.
		"""
		if self.save_file is None:
			self.save_file = ''.join(random.choice(string.ascii_uppercase 
							+ string.ascii_lowercase + string.digits) 
							for _ in range(16)) + '.csv'
			with open(self.save_file, 'w+') as save_file:
				csv.DictWriter(save_file, Budget.field_names).writeheader()
		else:
			with open(self.save_file) as save_file:
 				for row in csv.DictReader(save_file):
 					if row['deleted'] == 'False':
	 					self.create_expense_rec(
	 						row['id_'],
	 						row['name'],
	 						row['from_'],
	 						row['to'],
	 						row['current'])

	def create_expense_rec(self, id_, name, from_, to, start_val):
		"""Adds an ExpenseRec object to the expenses_rec list.
		"""
		new = ExpenseRec(id_, name, from_, to, start_val)
		self.expenses_rec.append(new)

	def save(self):
		""" Saves current app state to csv file save_file
		"""
		with open(self.save_file, 'w') as save_file:
			writer = csv.DictWriter(save_file, Budget.field_names)
			writer.writeheader()
			for expense_rec in self.expenses_rec:
				writer.writerow(
					{'id_' : expense_rec.id_,
					'name' : expense_rec.name,
					'from_': expense_rec.from_,
					'to' : expense_rec.to,
					'current': expense_rec.current,
					'deleted': expense_rec.deleted})

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






