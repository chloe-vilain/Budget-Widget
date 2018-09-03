"""Test.py
Test script which creates a new budget on the updated 
design paradigm
"""

from Budget import Budget
from GUI import GUI
from ExpenseRec import ExpenseRec
#import Tkinter as tk 

#Creates a new budget
chloe_budget = Budget(27000)
chloe_budget.create_expense_rec("Lodging", 0, 1000, 400)
chloe_budget.create_expense_rec("Car", 0, 700, 400)
chloe_budget.create_expense_rec("Health", 0, 500, 250)
chloe_budget.create_expense_rec("Food", 0, 400, 200)
chloe_budget.create_expense_rec("Subscriptions", 0, 200, 50)
chloe_budget.create_expense_rec("Incidental", 0, 800, 500)

#Test calculations for budget
#print chloe_budget.get_burndown_rate()
#print chloe_budget.get_months_remaining()

#Adds the GUI
chloe_budget_gui = GUI(chloe_budget)
chloe_budget_gui.mainloop()
