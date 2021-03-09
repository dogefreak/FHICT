year = int(input("Enter a year: "))
leapyear = False
#
# Write your code here.
#
if year % 4 != 0: leapyear = False
elif year % 100 != 0: leapyear = True
elif year % 400 != 0: leapyear = False
else: leapyear = True


# Write shit to console
if year >=0:
    if leapyear: print("That's a leap year!")
    else: print("That's a common year...")
else: print("That year isn't within the Gregorian calendar period!")