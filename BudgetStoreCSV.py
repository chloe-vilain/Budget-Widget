
from BudgetStore import BudgetStore
from Budget import Budget
import random
import string
import csv 

class BudgetStoreCSV(BudgetStore):

	def create(self, location = None):
		""" Creates  new CSV files: file to track expenses.
		Returns location_exp: str - save file name
		If passed a save name, will name files accordingly; else, 
		will generate random names. 
		"""
		if location is None:
			location = ''.join(random.choice(string.ascii_uppercase 
						+ string.ascii_lowercase + string.digits) 
						for _ in range(16))
		location_exp = '%s_exp.csv' %location
		with open(location_exp, 'w+') as save_file:
				csv.DictWriter(save_file, BudgetStore.field_names_exp).writeheader()
		return location_exp

	def read(self, savings, location):
		"""
		Creates a budget object by reading a CSV from a given location.
		Uses savings param since savings is not currently storable.
		"""
		budget = Budget(savings)
		with open(location) as save_file:
 			for row in csv.DictReader(save_file):
 				if row['deleted'] == 'False':
 					budget.create_expense_rec(
 						row['id_'],
 						row['name'],
 						row['from_'],
 						row['to'],
 						row['current'])
	 	return budget

	def write(self, budget, location):
		"""
		Writes a budget object to a CSV in a given location.
		"""
		with open(location, 'w') as save_file:
			writer = csv.DictWriter(save_file, fieldnames = BudgetStore.field_names_exp)
			writer.writeheader()
			for expense in budget.expenses_rec:
				writer.writerow(
					{'id_' : expense.id_,
					'name' : expense.name,
					'from_': expense.from_,
					'to' : expense.to,
					'current': expense.current,
					'deleted': expense.deleted})

