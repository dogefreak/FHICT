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
    #import xml.etree.ElementTree as ET
    from urllib.request import urlopen
    from lxml import etree
except:
    print("Problem with XML parser, please install 'lmxl' using 'pip3 install lxml'!")
    time.sleep(5)
    exit()

#Create global variables
disablefriday = False
disableweekend = True
path = "https://opendata.rijksoverheid.nl/v1/sources/rijksoverheid/infotypes/schoolholidays/schoolyear/2020-2021"

usehttp = True
vacation = False
data = []
startdates = []
enddates = []

#Create absolute path
here = os.path.dirname(os.path.abspath(__file__))
configini = os.path.join(here, 'config.ini')

#Read settings from config file, or create file
def settings():
    config = ConfigParser()
    
    #Create config file if it doesn't exist
    def checkcreate(message):
        global path, synergypath, disablefriday, disableweekend, enablesynergy
        if not os.path.exists('config.ini'):
            config['Configuration'] = {'disablefriday': str(disablefriday),
                                       'disableweekend': str(disableweekend),
                                       'path': str(path)}
            with open(configini, 'w') as configfile:
                config.write(configfile)
                print(message)       
                
    checkcreate("Config file was written in same path as this script!\n")

    #Read config file and assign variables
    def readconfig():
        global path, disablefriday, disableweekend
        config.read(configini)
        disablefriday = config.getboolean('Configuration', 'disablefriday')
        disableweekend = config.getboolean('Configuration', 'disableweekend')
        path = config.get('Configuration', 'path')

    #Try to read config, if exception: remove config and create new one and read it again
    try: readconfig()
    except:
        os.remove(configini)
        checkcreate("Corrupted file detected, created new config!\n\n")
        readconfig()


def read_xml():
    global path, vacation, data, startdates, enddates, usehttp
    
    def parse(f):
        global data
            
        tree = etree.parse(f)
        root = tree.getroot()

        vacationlist = root[3][0][2]
        index = -1
        
        for v in vacationlist:
            for w in v:
                for x in w:
                    if x.text == 'zuid' or x.text == 'heel Nederland':
                        y = x.getparent()
                        for z in y:
                            index += 1
                            if index % 3:
                                short = z.text.split(".", 1)
                                data.append(short[0])
                                #data.append(z.text)
    try:
        if usehttp:
            with urlopen(path) as f:
                parse(f)
        else: parse(path)
    except:
        vacation = True
        print("XML File not found!")

    for x in range(len(data)):
        date = datetime.datetime.strptime(data[x], '%Y-%m-%dT%H:%M:%S')
        if not x % 2: startdates.append(date)
        else: enddates.append(date)
        #print(date)

    vacationcheck = False

    for x in range(len(startdates)):
        if startdates[x] < datetime.datetime.now() < enddates[x]:
            vacationcheck = True
        else: vacation = False

    if vacationcheck is True: vacation = True
        
def main():
    
    global path, disablefriday, disableweekend, vacation, usehttp

    settings()

    if 'http' in path: usehttp = True
    else: usehttp = False

    read_xml()

    #If settings are True, enable vacation boolean as True
    if datetime.datetime.today().weekday() == 4 and disablefriday == True: vacation = True
    if datetime.datetime.today().weekday() == 5 or datetime.datetime.today().weekday() == 6 and disableweekend == True: vacation = True

    #If vacation bool is True: celebrate
    if vacation is True:
        print("Weekend / vacation!!!")
        time.sleep(1)
        exit()

    #If vacation is false: do something
    if vacation is False:
        print("Schoolday :(")
        #Or do something ;)
main()


