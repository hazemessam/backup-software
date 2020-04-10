from getpass import getpass


def accessAllowed():    
    password = getpass('password: ')
    if password == '':
        return True
    else:
        return False
