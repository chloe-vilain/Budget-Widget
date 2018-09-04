
from BudgetStore import BudgetStore
import random
import string
import csv 

class BudgetStoreCSV(BudgetStore):

	def create(self):
		""" Creates a new CSV file with a random alphanumeric name. Returns 
		"""
		location = ''.join(random.choice(string.ascii_uppercase 
						+ string.ascii_lowercase + string.digits) 
						for _ in range(16)) + '.csv'
		with open(location, 'w+') as save_file:
				csv.DictWriter(save_file, BudgetStore.field_names).writeheader()
		return location


	def read(self, location):
		print 'foo'

	def write(self, expenses, location):
		with open(location, 'w') as save_file:
			writer = csv.DictWriter(save_file, BudgetStore.field_names)
			writer.writeheader()
			for expense in expenses:
				writer.writerow(
					{'id_' : expense.id_,
					'name' : expense.name,
					'from_': expense.from_,
					'to' : expense.to,
					'current': expense.current,
					'deleted': expense.deleted})

