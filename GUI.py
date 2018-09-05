import Tkinter as tk
from Budget import Budget
from ExpenseRec import ExpenseRec

class GUI(tk.Frame):

	def __init__(self, budget, budget_store, master = None):
		""" Takes a Budget object and creates the GUI framework.
		Calls create_widgets to instanciate all visual elements.
		"""
		#self.budget = budget
		tk.Frame.__init__(self, master)
		self.expenses_rec = []
		self.grid()
		self.create_widgets(budget, budget_store)

	def create_widgets(self, budget, budget_store):
		""" Creates all hard-coded widgets in the budget application. 
		Iterates over expense objects in the GUI's budget and calls 
		create_expense_slider to instanciate them.   
		"""
		for expense_rec in budget.expenses_rec:
			self.create_expense_slider(expense_rec, budget)	
		self.create_budget_status(budget)
		self.create_save_button(budget_store)
		self.create_quit_button()

	def create_expense_slider(self, expense_rec, budget):
		"""Creates an expense slider and adds it to the grid. 
		Callback command will update the current value of the recurring 
		expense and update the budget status string.
		"""
		self.expenses_rec.append(tk.Scale(self, 
			orient = tk.HORIZONTAL, 
			from_ = expense_rec.from_,
			to = expense_rec.to, 
			length = 300,
			label = expense_rec.name, 
			command = lambda x:[expense_rec.set_current(x), self.update_budget_status(budget)])
		)
		self.expenses_rec[-1].set(expense_rec.current)
		self.expenses_rec[-1].grid()

	def create_budget_status(self, budget):
		"""Create budget status string and adds it to the grid"""
		self.budget_status = tk.Label()
		self.update_budget_status(budget)
		self.budget_status.grid()

	def create_save_button(self, budget_store):
		"""Creates a save button and adds it to the grid"""
		self.save_button = tk.Button(self, text = 'Save', command = budget_store.write)
		self.save_button.grid()

	def create_quit_button(self):
		"""Creates the quit button and adds it to the grid"""
		self.quit_button = tk.Button(self, text = 'Quit', command = self.quit)
		self.quit_button.grid()

	def update_budget_status(self, budget):
		"""Updates the budget status string. Called when a slider is updated."""
		m = budget.get_months_remaining()
		b = budget.get_burndown_rate()
		self.budget_status.configure(text = "Monthly burndown: %r Total months: %r" % (b, m))


