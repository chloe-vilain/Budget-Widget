from ExpenseRec import ExpenseRec

class Budget(object):
	"""Class for calculating my budget based on fixed and variable costs, which 
	can be set from the GUI class
	"""

	def __init__(self, savings):
		""" Initialize the budget program
		"""
		self.savings = savings
		self.expenses_rec = []

	def create_newExpenseRec(self, name, from_, to, start_val):
		self.expenses_rec.append(ExpenseRec(name, from_, to, start_val))

	def get_burndown_rate(self):
		""" Return the monthly burn-down rate based on all known costs
		"""
		#start = self.lodging_mon + self.car_mon + self.health_mon + self.food_mon + self.subscription_mon + self.gas_mon + self.fixed_costs_mon + self.incidental_mon
		start = 0 
		for expense_rec in self.expenses_rec:
			start = start + int(expense_rec.current)
		return start

	def get_months_remaining(self):
		return self.savings/ self.get_burndown_rate()



