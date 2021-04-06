# Function to validate the password 
def password_check(passwd): 
      
    SpecialSym =['$', '@', '#', '%', '!', '_'] 
    valid = False
    errorstring = "\nYour password should at least contain: "
      
    if len(passwd) < 6: errorstring = errorstring + '6 characters, '
    if len(passwd) > 20: errorstring = errorstring + 'less than 20 characters, '
    if not any(char.isdigit() for char in passwd): errorstring = errorstring + 'one numeral, ' 
    if not any(char.isupper() for char in passwd): errorstring = errorstring + 'an uppercase letter, '
    if not any(char.islower() for char in passwd): errorstring + 'a lowercase letter, '
    if not any(char in SpecialSym for char in passwd): errorstring = errorstring + 'special characters like "' + ''.join(SpecialSym) + '"'
    if errorstring == "\nYour password should at least contain: ": valid = True
    if valid is False: print(errorstring + "...")
    return valid   
  
# Main method
def main():
    passwd = input("Tell me your secrets: ") 
    
    while True: 
        if (password_check(passwd)): 
            print("\nPassword is valid <3")
            break
        else: 
            print("Your password is invalid! :(")
            passwd = input("\nTry again: ")
          
main() 
