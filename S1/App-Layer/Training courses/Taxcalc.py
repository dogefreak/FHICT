income = float(input("Enter the annual income: "))

#
# Write your code here.
#
if income >= 85528: tax = 14838 + (income - 85525)*0.32
if income < 85528: tax = income * 0.18 - 556.02
if income <= 0: tax = 0.0


tax = round(tax, 0)
print("The tax is:", tax, "thalers")
