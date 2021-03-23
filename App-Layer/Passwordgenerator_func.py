##Import random genarator library
import random

#Define default characters
default_pass = "qwertyuiopasdfgjklzxcvbnm"
length = ""

#Predefine question answers
no = ["n", "N", "no", "No", "NO", "nein"]
yes = ["y", "Y", "yes", "Yes", "YES", "aye", "ok"]

#Create bool
securitymessage = False

def numbchecker():
    global length
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
            print("\nThat's not a number, try again!\n")

def charchecker(state, answer):
    global default_pass
    global securitymessage
    loop = True
    while loop:
        if answer in yes:
            if state == "any_numbers1": default_pass = default_pass = default_pass + "0123456789"
            elif state == "any_specchar1": default_pass = default_pass + "[];',./!@#$%^&*()_+:<>?"
            elif state == "any_uppercase1": default_pass = default_pass + "QWERTYUIOPASDFGHJKLZXCVBNM"
            else: print("There's been an exception! :(")
            loop = False
            break 
        if answer in no:
            securitymessage = True
            if state == "any_numbers1": print("It's ill-advised to have a password without any numbers!")
            elif state == "any_specchar1": print("It's ill-advised to have a password without any special characters!")
            elif state == "any_uppercase1": print("It's ill-advised to have a password without any uppercase letters!")
            else: print("There's been an exception! :(")
            loop = False
            break
        else:
            print("\nYou didn't specifiy your choise...\n" + "Try again!")
            if state == "any_numbers1":
                consoleinput(number = "1")
            elif state == "any_specchar1":
                consoleinput(number = "2")
            elif state == "any_uppercase1":
                consoleinput(number = "3")
            else: print("There's been an exception! :(")
            break

def consoleinput(number):
    if number == "1":
        any_numbers = input("\nDo you want any numbers? (y/n): ")
        charchecker(state = "any_numbers1", answer = any_numbers)
    elif number == "2":
        any_specchar = input("\nDo you want any special characters? (y/n): ")
        charchecker(state = "any_specchar1", answer = any_specchar)
    elif number == "3":
        any_uppercase = input("\nDo you want any capital letters? (y/n): ")
        charchecker(state = "any_uppercase1", answer = any_uppercase)
    else: print("There's been an exception! :(")

def main():
    #Ask for number of required characters
    numbchecker()
    #Ask if user wants any numbers in their password
    consoleinput(number = "1")
    #Ask if user wants any special characters in their password
    consoleinput(number = "2")
    #Ask if user wants capital letters in their password
    consoleinput(number = "3")

    try:
        #Generate password and print it to the console, give warning if there's been a previous warning.
        generator = "".join(random.sample(default_pass, length))
        if securitymessage: print("\nYou didn't choose all availible options so your password might be compromised!")
        print("\nYour randomly generated password is:\n" + generator + "\n\nThank you for using this password generator!")
    except ValueError:
        print("\nThere's been an unknown error, please try again.\n")
        main()

#Run main function
main()
