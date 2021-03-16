##Import random genarator library
import random

#Define default characters
default_pass = "qwertyuiopasdfgjklzxcvbnm"

#Define question answers
no = ["n", "N", "no", "No", "NO", "nein"]
yes = ["y", "Y", "yes", "Yes", "YES", "aye"]

#Create bools
securitymessage = False
numericcheck = True

#Ask for password length, and check if it's an integer. If it's lower than 6 print a warning.
while numericcheck:
    try:
        length = int(input("Specify your required password length: "))
        length = int(length)
        if length < 6:
            securitymessage = True
            print("It's ill-advised to have a password under the length of 6 characters!")
        numericcheck = False
        break
    except ValueError:
        print("\nThat not a number, try again!\n")

#Ask if user wants any numbers in their password, give warning if disabled or enable when invalid input.
any_numbers = input("\nDo you want any numbers? (y/n): ")

if any (ele in any_numbers for ele in yes):
    default_pass = default_pass + "0123456789"
elif any (ele in any_numbers for ele in no):
    securitymessage = True
    print("It's ill-advised to have a password without any numbers!")
else:
    print("\nYou didn't specifiy your choise...\n" + "Enabling numbers during generation (default option)...\n")
    default_pass = default_pass + "0123456789"

#Ask if user wants any special chars in their password, give warning if disabled or enable when invalid input.
any_specchar = input("\nDo you want any special characters? (y/n): ")

if any (ele in any_specchar for ele in yes):
    default_pass = default_pass + "[];',./!@#$%^&*()_+:<>?"
elif any (ele in any_specchar for ele in no):
    securitymessage = True
    print("It's ill-advised to have a password without any special characters!")
else:
    print("\nYou didn't specifiy your choise...\n" + "Enabling special characters during generation (default option)...\n")
    default_pass = default_pass + "[];',./!@#$%^&*()_+:<>?"

#Ask if user wants any capital letters in their password, give warning if disabled or enable when invalid input.
any_uppercase = input("\nDo you want any uppercase letters? (y/n): ")

if any (ele in any_uppercase for ele in yes):
    default_pass = default_pass + "QWERTYUIOPASDFGHJKLZXCVBNM"
elif any (ele in any_uppercase for ele in no):
    securitymessage = True
    print("It's ill-advised to have a password without any uppercase letters!")
else:
    print("\nYou didn't specifiy your choise...\n" + "Enabling captital letters during generation (default option)...")
    default_pass = default_pass + "QWERTYUIOPASDFGHJKLZXCVBNM"


#Generate password and print it to the console, give warning if there's been a previous warning.
generator = "".join(random.sample(default_pass, length))

if securitymessage: print("\nYou didn't choose all availible options so your password might be compromised!\n\n")
print("Your randomly generated password is:\n" + generator)

