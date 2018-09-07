from Budget import Budget
from BudgetStore import BudgetStore
from BudgetStoreCSV import BudgetStoreCSV
from BudgetStoreJSON import BudgetStoreJSON
from GUI import GUI

class Application(object):

	budget_store_types = {
		'csv' : BudgetStoreCSV,
		'json' : BudgetStoreJSON
	}

	def __init__(self, location = None, budget_store_prefer = 'csv', savings = 27000):
		"""
		Controller class. 
		Builds budget from a save, if save exists. 
		If not, builds a new budget with default store type csv
		"""
		self.location = location
		if budget_store_prefer not in Application.budget_store_types:
			raise KeyError('Budget Store preference not recognized')
		self.budget_store = Application.budget_store_types[budget_store_prefer]()
		self.budget = self.generate_budget(savings)
		self.GUI = GUI(self.budget, self.location, self.budget_store)
		self.GUI.mainloop()

	def generate_budget(self, savings):
		if self.location is not None:
			return self.budget_store.read(savings, self.location)
		else: 
			self.location = self.budget_store.create()
			budget = Budget(savings)
			self.add_initial_expenses(budget)
			return budget

	def add_initial_expenses(self, budget):
		"""TO DEPRECATE
		Function added to test creating new sliders, w/o having 
		to add a UI flow to add sliders. 
		"""
		budget.create_expense_rec(1, "Lodging", 0, 1000, 400)
		budget.create_expense_rec(2, "Car", 0, 700, 400)
		budget.create_expense_rec(3, "Health", 0, 500, 250)
		budget.create_expense_rec(4, "Food", 0, 400, 200)
		budget.create_expense_rec(5, "Subscriptions", 0, 200, 50)





