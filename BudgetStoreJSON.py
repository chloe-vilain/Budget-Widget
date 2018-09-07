from BudgetStore import BudgetStore
from Budget import Budget
import json
import string
import random

class BudgetStoreJSON(BudgetStore):

	def create(self, location = None):
		"""Generates new json filename to be used for saves
		"""
		if location is None:
			location = ''.join(random.choice(string.ascii_uppercase 
						+ string.ascii_lowercase + string.digits) 
						for _ in range(16))
		location_exp = '%s_exp.json' %location
		return location_exp

	def read(self, location):
		""" Reads budget from a given json file (location)
		"""
		budget = None
		with open(location, "r") as save_file:
			data = json.load(save_file)
			budget = Budget(data["savings"])
			for expense in data["expenses_rec"]:
				budget.create_expense_rec(
					expense["id_"],
					expense["name"],
					expense["from_"],
					expense["to"],
					expense["current"])
		return budget
		 

	def write(self, budget, location):
		""" writes a budget object to a json file with the specified 
		write location (file name)
		"""
		savings = budget.savings
		expenses_rec = self.expense_recs_to_list(budget.expenses_rec)
		my_json = {"savings" : savings, "expenses_rec" : expenses_rec}
		with open(location, "w+") as save_file:
			json.dump(my_json, save_file, indent = 4)

	def expense_recs_to_list(self, expenses_rec):
		""" Converts a budget's expenses_rec list to dictionary format for the 
		JSON writer
		"""
		return [self.expense_rec_to_dict(expense_rec) for expense_rec in expenses_rec]

	def expense_rec_to_dict(self, expense_rec):
		""" Converts an individual expense to dictionary format for the JSON writer
		"""
		return {
				"id_" : expense_rec.id_,
				"name" : expense_rec.name,
				"from_" : expense_rec.from_,
				"to" : expense_rec.to,
				"current" : expense_rec.current
				}

		


