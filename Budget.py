
class Budget(object):
	"""Class for calculating my budget based on fixed and variable costs, which 
	can be set from the GUI class
	"""

	def __init__(self, savings, lodging_mon, gas_mon, fixed_costs_mon, incidental_mon):
		""" Initialize the budget program
		"""
		self.savings = savings
		self.lodging_mon = lodging_mon
		self.gas_mon = gas_mon
		self.fixed_costs_mon = fixed_costs_mon
		self.incidental_mon = incidental_mon

	def get_burndown_rate(self):
		""" Return the monthly burn-down rate based on all known costs
		"""
		return self.lodging_mon + self.gas_mon + self.fixed_costs_mon + self.incidental_mon

	def get_months_remaining(self):
		return self.savings/ self.get_burndown_rate()

	def set_lodging_mon(self, new):
		self.lodging_mon = int(new)
		#print self.lodging_mon

	def set_incidental_mon(self, new):
		self.incidental_mon = int(new)
		#print type (self.incidental_mon)
		#print self.get_months_remaining()

my_budget = Budget(27000, 400, 100, 400, 400)
print my_budget.get_burndown_rate()
print my_budget.get_months_remaining()  


