year = input("Enter a year or type a letter to stop: ")
leapyear = False
loop = True

#
# Write your code here.
#

while loop:
    
    # Check if input is an int or disable loop
    try:
        int(year)
        year = int(year)
    except ValueError:
        loop = False
        print("\nBye!")
        break
    except TypeError:
        loop = False
        print("\nBye!")
        break

    #Maths stuff
    if year % 4 != 0: leapyear = False
    elif year % 100 != 0: leapyear = True
    elif year % 400 != 0: leapyear = False
    else: leapyear = True


    # Write shit to console
    if year >=0:
        if leapyear: print("That's a leap year!")
        else: print("That's a common year...")
    else: print("That year isn't within the Gregorian calendar period!")

    print(year)
    
    year = input("\nEnter another year or type a letter to stop: ")
       
