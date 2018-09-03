import Tkinter as tk
from Budget import Budget
from ExpenseRec import ExpenseRec

class GUI(tk.Frame):

	def __init__(self, budget, master = None):
		self.budget = budget
		tk.Frame.__init__(self, master)
		self.expensesRec = []
		self.grid()
		self.createWidgets()

	def createWidgets(self):
		for expense_rec in self.budget.expenses_rec:
			self.create_expense_slider(expense_rec)		
		self.create_budgetStatus()
		self.create_quitButton()

	def create_expense_slider(self, expenseRec):
		self.expensesRec.append(tk.Scale(self, 
			orient = tk.HORIZONTAL, 
			from_ = expenseRec.from_,
			to = expenseRec.to, 
			length = 300,
			label = expenseRec.name, 
			command = lambda x:[expenseRec.set_current(x), self.update_budgetStatus()])
		)
		self.expensesRec[-1].set(expenseRec.current)
		self.expensesRec[-1].grid()

	def create_budgetStatus(self):
		self.budgetStatus = tk.Label()
		self.update_budgetStatus()
		self.budgetStatus.grid()

	def create_quitButton(self):
		self.quitButton = tk.Button(self, text = 'Quit', command = self.quit)
		self.quitButton.grid()

	def update_budgetStatus(self):
		m = self.budget.get_months_remaining()
		b = self.budget.get_burndown_rate()
		self.budgetStatus.configure(text = "Monthly burndown: %r Total months: %r" %(b, m))


