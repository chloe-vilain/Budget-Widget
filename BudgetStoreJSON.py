from BudgetStore import BudgetStore
import json
import string
import random

class BudgetStoreJSON(BudgetStore):
	"""Abstract base class defining Store methods
	"""

	def create(self, location = None):
		if location is None:
			location = ''.join(random.choice(string.ascii_uppercase 
						+ string.ascii_lowercase + string.digits) 
						for _ in range(16))
		location_exp = '%s_exp.json' %location
		return location_exp

	def read(self, location):
		""" Read data from store

		parameters:
		- location: str - location to read data from 

		Returns budget: Budget - The Budget object leveraged by the application.
		"""
		return
		 

	def write(self, budget, location):
		savings = budget.savings
		expenses_rec = self.expense_recs_to_list(budget.expenses_rec)
		my_json = {"savings" : savings, "expenses_rec" : expenses_rec}
		with open(location, "w+") as save_file:
			json.dump(my_json, save_file, indent = 4)

	def expense_recs_to_list(self, expenses_rec):
		return [self.expense_rec_to_dict(expense_rec) for expense_rec in expenses_rec]

	def expense_rec_to_dict(self, expense_rec):
		return {
				"name" : expense_rec.name,
				"from" : expense_rec.from_,
				"to_" : expense_rec.to,
				"current" : expense_rec.current
				}
		


