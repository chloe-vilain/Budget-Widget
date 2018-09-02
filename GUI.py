import Tkinter as tk
from Budget import Budget

class GUI(tk.Frame):

	def __init__(self, budget, master = None):
		self.budget = budget
		tk.Frame.__init__(self, master)
		self.grid()
		self.createWidgets()

	def createWidgets(self):
		self.create_lodgingScale()
		self.create_carScale()
		self.create_incidentalScale()	
		self.create_budgetStatus()
		self.create_quitButton()

	def create_lodgingScale(self, from_ = 0, to = 1000, length = 300):
		self.lodgingScale = tk.Scale(self, orient=tk.HORIZONTAL, from_ = from_, to = to, length = length, label = 'Lodging Cost', command = self.update_lodging_cost)
		self.lodgingScale.set(self.budget.lodging_mon)
		self.lodgingScale.grid()

	def create_carScale(self, from_ = 0, to = 700, length = 300):
		self.carScale = tk.Scale(self, orient=tk.HORIZONTAL, from_ = from_, to = to, length = length, label = 'Car Cost', command = self.update_car_cost)
		self.carScale.set(self.budget.car_mon)
		self.carScale.grid()


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

	def update_incidental_cost(self, new):
		self.budget.set_incidental_mon(new)
		self.update_budgetStatus()

	def update_budgetStatus(self):
		m = self.budget.get_months_remaining()
		b = self.budget.get_burndown_rate()
		self.budgetStatus.configure(text = "Monthly burndown: %r Total months: %r" %(b, m))

my_budget = Budget(27000, 400, 400, 100, 400, 400)
app = GUI(my_budget)
app.master.title('Budget Application')
app.mainloop()

