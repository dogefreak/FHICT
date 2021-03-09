# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Choose the larger number
temp_largest = number1

if temp_largest < number2: temp_largest = number2
if temp_largest < number3: temp_largest = number3

perm_largest = temp_largest

# Print the result
print("The larger number is:", perm_largest)
