"""Test.py
Test script which creates a new budget on the updated 
design paradigm
"""

from Budget import Budget
from GUI import GUI
from ExpenseRec import ExpenseRec
#import Tkinter as tk 

#Creates a new budget
"""chloe_budget = Budget(27000)
chloe_budget.create_expense_rec(1, "Lodging", 0, 1000, 400)
chloe_budget.create_expense_rec(2, "Car", 0, 700, 400)
chloe_budget.create_expense_rec(3, "Health", 0, 500, 250)
chloe_budget.create_expense_rec(4, "Food", 0, 400, 200)
chloe_budget.create_expense_rec(4, "Subscriptions", 0, 200, 50)
chloe_budget.create_expense_rec(5, "Incidental", 0, 800, 500)"""

#Opens an existing budget
chloe_budget = Budget(27000, 'Iwo3GwPQGNdd9y35.csv')


#Test calculations for budget
#print chloe_budget.get_burndown_rate()
#print chloe_budget.get_months_remaining()

#Adds the GUI
chloe_budget_gui = GUI(chloe_budget)
chloe_budget_gui.mainloop()
