
from BudgetStore import BudgetStore
import random
import string
import csv 

class BudgetStoreCSV(BudgetStore):

	def create(self, location = None):
		""" Creates two new CSV files: file to track expenses, 
		file with application data. Returns a tuple of files. 
		If passed a save name, will name files accordingly; else, 
		will generate random names. 
		"""
		if location is None:
			location = ''.join(random.choice(string.ascii_uppercase 
						+ string.ascii_lowercase + string.digits) 
						for _ in range(16))
		location_exp = '%r_exp.csv' %location
		with open(location_exp, 'w+') as save_file:
				csv.DictWriter(save_file, BudgetStore.field_names_exp).writeheader()
		return location_exp

	def read(self, location):
		print 'foo'

	def write(self, expenses, location):
		with open(location, 'w') as save_file:
			writer = csv.DictWriter(save_file, BudgetStore.field_names_exp)
			writer.writeheader()
			for expense in expenses:
				writer.writerow(
					{'id_' : expense.id_,
					'name' : expense.name,
					'from_': expense.from_,
					'to' : expense.to,
					'current': expense.current,
					'deleted': expense.deleted})

