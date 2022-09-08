#This program will generate valid BSN

#Import Libraries
import random

#Generate random numbers
def bsnGen(number):
    for x in range(number):
        while True:
            chars = random.sample(range(0, 9), 9)
            som = 9*chars[0] + 8*chars[1] + 7*chars[2] + 6*chars[3] + 5*chars[4] + 4*chars[5] + 3*chars[6] + 2*chars[7] + -1*chars[8]
            maths = som % 11
            if maths == 0:
                print("\n", *chars, sep="")
                break

#Verify the answer of any question
def check(question):
    while True:
        check1 = input(question + " ([y]/n): ")
        if check1 == "y": return True
        elif check1 == "n": return False
        elif check1 == "": return True
        else: print('\nThe question must be answered with "y" or "n"!')

#Check if input is an int
def intCheck():
    while True:
        number = input("\nHow many BSNs do you want?: ")
        if number.isdigit():
            number = int(number)
            bsnGen(number)
            break
        else: print("\nPlease try again!")        

#Main function
def main():
    print("Welcome to the BSN genarator!")
    while True:
        tryit = check("\nDo you want one?")
        if tryit is True:
            intCheck()
        else: break
    print("\nCiao!")
    exit()

main()
