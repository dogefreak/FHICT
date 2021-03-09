# Function to validate the password 
def password_check(passwd): 
      
    SpecialSym =['$', '@', '#', '%', '!', '_'] 
    valid = True
    errorstring = "\nYour password should at least contain: "
      
    if len(passwd) < 6:
        errorstring = errorstring + '6 characters, ' 
        valid = False
          
    if len(passwd) > 20:
        errorstring = errorstring + 'less than 20 characters, '
        valid = False
          
    if not any(char.isdigit() for char in passwd):
        errorstring = errorstring + 'one numeral, ' 
        valid = False
          
    if not any(char.isupper() for char in passwd): 
        errorstring = errorstring + 'an uppercase letter, '
        valid = False
          
    if not any(char.islower() for char in passwd): 
        errorstring + 'a lowercase letter, '
        valid = False
          
    if not any(char in SpecialSym for char in passwd): 
        charlist = ''.join(SpecialSym)
        errorstring = errorstring + 'special characters like "' + charlist + '"'
        valid = False
        
    if valid: 
        return valid
    if valid is False:
        print(errorstring + "...")
  
# Main method 
def main():
    invalid = True
    passwd = input("Tell me your secrets: ") 
    
    while invalid: 
        if (password_check(passwd)): 
            print("\nPassword is valid <3")
            invalid = False
            break
        else: 
            print("Your password is invalid! :(")
            passwd = input("\nTry again: ") 
          
main() 
