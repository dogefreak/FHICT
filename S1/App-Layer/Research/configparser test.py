import configparser
config = configparser.ConfigParser()
config['Requirements'] = {'minlength': '6',
                          'maxlength': '20',
                          'numbers': 'true',
                          'uppercase': 'true',
                          'lowercase': 'true',
                          'punctuation': 'true'}
with open('config.ini', 'w') as configfile:
    config.write(configfile)

