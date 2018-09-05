from Budget import Budget
from BudgetStore import BudgetStore
from BudgetStoreCSV import BudgetStoreCSV
from GUI import GUI

class Application(object):

	def __init__(self, save = None, budget_store_prefer = 'csv', savings = 27000):
		"""
		Controller class. 
		Builds budget from a save, if save exists. 
		If not, builds a new budget with default store type csv
		"""
		self.budget_store = self.choose_budget_store(budget_store_prefer)
		if save is not None:
			self.budget = self.budget_store.read(save)
		else: 
			self.budget = Budget(savings)
		self.add_initial_expenses()
		self.GUI = GUI(self.budget, self.budget_store)
		self.GUI.mainloop()


	def choose_budget_store(self, budget_store_prefer):
		""" Returns a budget store object based on preference passed.
		"""
		if budget_store_prefer == 'csv':
			return BudgetStoreCSV()
		else:
			raise ValueError('Budget store preference not recognized')

	def add_initial_expenses(self):
		self.budget.create_expense_rec(1, "Lodging", 0, 1000, 400)
		self.budget.create_expense_rec(2, "Car", 0, 700, 400)
		self.budget.create_expense_rec(3, "Health", 0, 500, 250)
		self.budget.create_expense_rec(4, "Food", 0, 400, 200)
		self.budget.create_expense_rec(5, "Subscriptions", 0, 200, 50)





