#Import libraries
try:
    import os
    from configparser import ConfigParser
    succes = True
except (ModuleNotFoundError, ImportError) as e:
    print("There's been an error with the config, using default settings.\n\n")
try:
    import datetime
    import time
except (ModuleNotFoundError, ImportError) as e:
    print("Error with timing... closing script :(")
    time.sleep(3)
    exit()
try:
    import xml.etree.ElementTree as ET
    from urllib.request import urlopen
except: print("Problem with XML parser!")

#Create global variables
enablesynergy = True
disablefriday = True
disableweekend = True
synergypath = "/Applications/Synergy.app"
url = "https://opendata.rijksoverheid.nl/v1/sources/rijksoverheid/infotypes/schoolholidays/schoolyear/2020-2021"

vacation = False
data = []

#Read settings from config file, or create file    
config = ConfigParser()

#Create config file if it doesn't exist
def checkcreate(message):
    global url, synergypath, disablefriday, disableweekend, enablesynergy
    if not os.path.exists('config.ini'):
        config['Configuration'] = {'disablefriday': str(disablefriday),
                                   'disableweekend': str(disableweekend),
                                   'enablesynergy': str(enablesynergy),
                                   'synergypath': str(synergypath),
                                   'url': str(url)}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
            print(message)

#Read config file and assign variables
def readconfig():
    global url, synergypath, disablefriday, disableweekend, enablesynergy
    config.read('config.ini')
    disablefriday = config.getboolean('Configuration', 'disablefriday')
    disableweekend = config.getboolean('Configuration', 'disableweekend')
    enablesynergy = config.getboolean('Configuration', 'enablesynergy')
    synergypath = config.get('Configuration', 'synergypath')
    url = config.get('Configuration', 'url')


def read_xml():

    global url, vacation, data

    inputID = ['zuid', 'heel Nederland']

    with urlopen(url) as f:
        tree = ET.parse(f)
        root = tree.getroot()
        vacationlist = root[3][0][2]

        continueagain: False
        continuemore: False

        for x in vacationlist:
            for y in x:
                for z in y:
                    data = z.text
                    

        
def main():

    global url, synergypath, disablefriday, disableweekend, enablesynergy, vacation

    checkcreate("Config file was written in same path as this script!\n\n")

    #Try to read config, if exception: remove config and create new one and read it again
    try: readconfig()
    except:
        os.remove('config.ini')
        checkcreate("Corrupted file detected, created new config!\n\n")
        readconfig()

    #If settings are True, enable vacation boolean as True
    if datetime.datetime.today().weekday() == 4 and disablefriday == True: vacation = True
    if datetime.datetime.today().weekday() == 5 or datetime.datetime.today().weekday() == 6 and disableweekend == True: vacation = True

    read_xml()

    #If vacation bool is True: celebrate
    #if vacation is True: exit()

    #If vacation is false: open synergy, open teamsbot
    
    if vacation is False:
        null = 0

        #Open synergy
        #os.system("open " + str(synergypath))
        #time.sleep(10)
        #Autohide?
        #os.system("""osascript -e 'tell app "Synergy" to close every window'""")

        #Try to join meeting every minute

    print(vacation)
    print(disablefriday)

main()


