import Tkinter as tk
from Budget import Budget
from Expense_Rec import Expense_Rec

class GUI(tk.Frame):

	def __init__(self, budget, master = None):
		self.budget = budget
		tk.Frame.__init__(self, master)
		self.expensesRec = []
		self.grid()
		self.createWidgets()

	def createWidgets(self):
		self.create_lodgingScale()
		self.create_carScale()
		self.create_healthScale()
		self.create_foodScale()
		self.create_subscriptionScale()	
		self.create_incidentalScale()
		for expense_rec in self.budget.expenses_rec:
			self.create_newExpenseRec(expense_rec)
		self.create_budgetStatus()
		self.create_quitButton()

	def create_newExpenseRec(self, expenseRec):
		self.expensesRec.append(tk.Scale(self, orient = tk.HORIZONTAL, from_ = expenseRec.from_, to = expenseRec.to, length = 300, label = expenseRec.name, command = lambda x:[expenseRec.set_current(x), self.update_budgetStatus()]))
		self.expensesRec[-1].set(expenseRec.current)
		self.expensesRec[-1].grid()


	def create_lodgingScale(self, from_ = 0, to = 1000, length = 300):
		self.lodgingScale = tk.Scale(self, orient=tk.HORIZONTAL, from_ = from_, to = to, length = length, label = 'Lodging Cost', command = self.update_lodging_cost)
		self.lodgingScale.set(self.budget.lodging_mon)
		self.lodgingScale.grid()

	def create_carScale(self, from_ = 0, to = 700, length = 300):
		self.carScale = tk.Scale(self, orient = tk.HORIZONTAL, from_ = from_, to = to, length = length, label = 'Car Cost', command = self.update_car_cost)
		self.carScale.set(self.budget.car_mon)
		self.carScale.grid()

	def create_healthScale(self, from_ = 0, to = 500, length = 300):
		self.healthScale = tk.Scale(self, orient = tk.HORIZONTAL, from_ = from_, to = to, length = length, label = 'Health Scale', command = self.update_health_cost)
		self.healthScale.set(self.budget.health_mon)
		self.healthScale.grid()

	def create_foodScale(self, from_ = 0, to = 400, length = 300):
		self.foodScale = tk.Scale(self, orient = tk.HORIZONTAL, from_ = from_, to = to, length = length, label = 'Food Scale', command = self.update_food_cost)
		self.foodScale.set(self.budget.food_mon)
		self.foodScale.grid()		

	def create_subscriptionScale(self, from_ = 0, to = 200, length = 300):
		self.subscriptionScale = tk.Scale(self, orient = tk.HORIZONTAL, from_ = from_, to = to, length = length, label = 'Subscription Scale', command = self.update_subscription_cost)
		self.subscriptionScale.set(self.budget.subscription_mon)
		self.subscriptionScale.grid()

	def create_incidentalScale(self, from_ = 0, to = 1000, length = 300):
		self.incidentalScale = tk.Scale(self, orient=tk.HORIZONTAL, from_ = from_, to = to, length = length, label = 'Incidental Cost', command = self.update_incidental_cost)
		self.incidentalScale.set(self.budget.incidental_mon)
		self.incidentalScale.grid()

	def create_budgetStatus(self):
		self.budgetStatus = tk.Label()
		self.update_budgetStatus()
		self.budgetStatus.grid()

	def create_quitButton(self):
		self.quitButton = tk.Button(self, text = 'Quit', command = self.quit)
		self.quitButton.grid()

	def update_lodging_cost(self, new):
		self.budget.set_lodging_mon(new)
		self.update_budgetStatus()

	def update_car_cost(self, new):
		self.budget.set_car_mon(new)
		self.update_budgetStatus()

	def update_health_cost(self, new):
		self.budget.set_health_mon(new)
		self.update_budgetStatus()

	def update_food_cost(self, new):
		self.budget.set_food_mon(new)
		self.update_budgetStatus()

	def update_subscription_cost(self, new):
		self.budget.set_subscription_mon(new)
		self.update_budgetStatus()

	def update_incidental_cost(self, new):
		self.budget.set_incidental_mon(new)
		self.update_budgetStatus()

	def update_budgetStatus(self):
		m = self.budget.get_months_remaining()
		b = self.budget.get_burndown_rate()
		print "foo"
		self.budgetStatus.configure(text = "Monthly burndown: %r Total months: %r" %(b, m))

my_budget = Budget(27000, 400, 400, 250, 200, 50, 100, 400, 400)
app = GUI(my_budget)
app.master.title('Budget Application')
app.mainloop()

