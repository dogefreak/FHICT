#This program will generate valid BSN

#Import Libraries
import random

#Generate random numbers
def bsnGen():
    while True:
        chars = random.sample(range(0, 9), 9)

        a = chars[0] * 9
        b = chars[1] * 8
        c = chars[2] * 7
        d = chars[3] * 6
        e = chars[4] * 5
        f = chars[5] * 4
        g = chars[6] * 3
        h = chars[7] * 2
        i = chars[8] * -1

        som = a+b+c+d+e+f+g+h+i

        maths = som % 11

        if maths == 0:
            print("\nSucces!\n")
            print(*chars)
            break
        else: continue

def check(question):
    while True:
        check1 = input(question + " ([y]/n): ")
        if check1 == "y":
            return True
        elif check1 == "n":
            return False
        elif check1 == "":
            return True
        else:
            print('\nThe question must be answered with "y" or "n"!')

def main():
    firsttry = check("Welcome to the BSN genarator, do you want one?")
    if firsttry is True: bsnGen()
    else: exit()
    
    while True:
        secondtry = check("\nDo you want another one?")
        if secondtry is True: bsnGen()
        else: break
    exit()

main()
