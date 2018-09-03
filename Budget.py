from Expense_Rec import Expense_Rec

class Budget(object):
	"""Class for calculating my budget based on fixed and variable costs, which 
	can be set from the GUI class
	"""

	def __init__(self, savings, lodging_mon, car_mon, health_mon, food_mon, subscription_mon, gas_mon, fixed_costs_mon, incidental_mon):
		""" Initialize the budget program
		"""
		self.savings = savings
		self.lodging_mon = lodging_mon
		self.car_mon = car_mon
		self.health_mon = health_mon
		self.food_mon = food_mon
		self.subscription_mon = subscription_mon
		self.gas_mon = gas_mon
		self.fixed_costs_mon = fixed_costs_mon
		self.incidental_mon = incidental_mon
		self.expenses_rec = []
		#example = Expense_Rec("test", 0, 100, 50)
		self.create_newExpenseRec("test", 0, 100, 50)

	def create_newExpenseRec(self, name, from_, to, start_val):
		self.expenses_rec.append(Expense_Rec(name, from_, to, start_val))

	def get_burndown_rate(self):
		""" Return the monthly burn-down rate based on all known costs
		"""
		start = self.lodging_mon + self.car_mon + self.health_mon + self.food_mon + self.subscription_mon + self.gas_mon + self.fixed_costs_mon + self.incidental_mon
		for expense_rec in self.expenses_rec:
			start = start + int(expense_rec.current)
		return start

	def get_months_remaining(self):
		return self.savings/ self.get_burndown_rate()

	def set_lodging_mon(self, new):
		self.lodging_mon = int(new)

	def set_incidental_mon(self, new):
		self.incidental_mon = int(new)

	def set_car_mon(self, new):
		self.car_mon = int(new)

	def set_health_mon(self, new):
		self.health_mon = int(new)

	def set_food_mon(self, new):
		self.food_mon = int(new)

	def set_subscription_mon(self, new):
		self.subscription_mon = int(new)
"""
my_budget = Budget(27000, 400, 400, 100, 400, 400)
print my_budget.get_burndown_rate()
print my_budget.get_months_remaining() 
""" 


