try: import string
except: print("Error with importing library!")

#Function to return if input is palindrome
def palindrome(i):
    l = ''.join([x for x in i.lower() if not x in string.punctuation]).replace(' ','')
    if len(l) >= 1: return l == l[::-1]
    else: return False

# Ask question, keep checking for palindrome
q = input("Enter your text: ")
while True: 
    if palindrome(q):
        print("\nYour input was in fact a palindrome!")
        break
    else: q = input("\nTry again: ")
