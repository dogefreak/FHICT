#Import libraries
try:
    import os
    import subprocess
    import sys
    import dns
    import dns.resolver as resolver
    from configparser import ConfigParser
except:
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install dnspython"])
        import dns
        import dns.resolver as resolver
    except: exit()

#Create global variables
receive = ['A', 'MX', 'NS', 'TXT', 'CNAME']
restart = False

#Read settings from config file, or create file
def config(path):
    config = ConfigParser()

    #Create config file if it doesn't exist
    def create(path, retry):
        if not os.path.exists(path):
            config['Configuration'] = {'A': 'True',
                                       'MX': 'True',
                                       'NS': 'True',
                                       'TXT': 'True',
                                       'CNAME': 'True'}
            with open(path, 'w') as configfile:
                config.write(configfile)
            if retry: print("Config file was corrupted, new file was created!\n\n")
            else: print("Created new config file! :)\n\n")

    #Read config file
    def read(path):
        config.read(path)
        for i in receive:
            if not config.getboolean('Configuration', i): receive.remove(i)

    #Try reading, or create new file
    try:
        create(path, False)
        read(path)
    except:
        os.remove(path)
        create(path, True)
        read(path)

#DNS-lookup
def lookup(url):
    global restart
    for i in receive:
        try:
            request = resolver.resolve(url, i)
            for result in request:
                print(i, "record: ", result)
        except dns.resolver.NoAnswer:
            print(i, "record: No Answer")
        except dns.rdatatype.UnknownRdatatype:
            pass
        except dns.resolver.NXDOMAIN:
            print("That domain doesn't exist!")
            restart = True
            break

def main():
    config('config.ini')
    while True:
        url = input("Enter a URL: ")
        lookup(url)
        if restart: pass
        else: break

main()
