#Import libraries
try:
    import os
    import string
    from configparser import ConfigParser
    succes = True
except (ModuleNotFoundError, ImportError) as e:
    print("There's been an error with the config, using default settings.\n\n")

#Create global variables
minlength = 6
maxlength = 20
numbers = True
uppercase = True
lowercase = True
punctuation = True

#Read settings from config file, or create file
def settings_check():
    config = ConfigParser()
    #Create config file if it doesn't exist
    if not os.path.exists('config.ini'):
        config['Requirements'] = {'minlength': '6',
                                  'maxlength': '20',
                                  'numbers': 'True',
                                  'uppercase': 'True',
                                  'lowercase': 'True',
                                  'punctuation': 'True'}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    #Read config file and assign variables        
    config.read('config.ini')
    minlength = config.get('Requirements', 'minlength')
    maxlength = config.get('Requirements', 'maxlength')
    numbers = config.getboolean('Requirements', 'numbers')
    uppercase = config.getboolean('Requirements', 'uppercase')
    lowercase = config.getboolean('Requirements', 'lowercase')
    punctuation = config.getboolean('Requirements', 'punctuation')

# Method to validate the password 
def password_check(passwd):
    errorstring = "\nYour password should at least contain: " 
    if len(passwd) < int(minlength): errorstring = errorstring + '\n* ' + str(minlength) + ' characters'
    if len(passwd) > int(maxlength): errorstring = errorstring + '\n* Less than ' + str(maxlength) + ' characters'
    if not any(char.isdigit() for char in passwd):
        if numbers is True: errorstring = errorstring + '\n* One numeral'
    if not any(char.isupper() for char in passwd):
        if uppercase is True: errorstring = errorstring + '\n* An uppercase letter'
    if not any(char.islower() for char in passwd):
        if lowercase is True: errorstring = errorstring + '\n* A lowercase letter'
    if not any(char in string.punctuation for char in passwd):
        if punctuation is True: errorstring = errorstring + '\n* A special character'
    if errorstring == "\nYour password should at least contain: ": return True
    else: print(errorstring)
  
# Main function
def main():
    if succes is True: settings_check()
    passwd = input("Tell me your secrets: ") 
    while True:
        if (password_check(passwd)): 
            print("\nPassword is valid <3")
            break
        else: 
            print("\nYour password is invalid! :(")
            passwd = input("\nTry again: ")
          
main()
