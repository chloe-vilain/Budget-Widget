import Tkinter as tk
from Budget import Budget

class GUI(tk.Frame):

	def __init__(self, budget, master = None):
		self.budget = budget
		tk.Frame.__init__(self, master)
		self.grid()
		self.createWidgets()

	def createWidgets(self):
		self.lodgingScale = tk.Scale(self, orient=tk.HORIZONTAL, from_ = 0, to = 1000, length = 300, label = 'Lodging Cost', command = self.budget.set_lodging_mon)
		self.incidentalScale = tk.Scale(self, orient=tk.HORIZONTAL, from_ = 0, to = 1000, length = 300, label = 'Incidental Cost', command = self.budget.set_incidental_mon)
		m = self.budget.get_months_remaining()
		self.budgetStatus = tk.Label(text = "Monthly burndown: foo Total months: %r" %m) #BUG HERE
		self.quitButton = tk.Button(self, text = 'Quit', command = self.quit)
		self.lodgingScale.grid()
		self.incidentalScale.grid()
		self.budgetStatus.grid()
		self.quitButton.grid()

my_budget = Budget(27000, 400, 100, 400, 400)
app = GUI(my_budget)
app.master.title('Budget Application')
app.mainloop()