import random
import string

def createPswd():
    # Declare collections of characters allowed to be used in the password
    data = ["","",""]
    may_letters = string.ascii_lowercase
    min_letters = string.ascii_uppercase
    numbers = "123456789"
    special_symbols = "[]{}()*;/,_-"
    success = False 
    data[0] = input("Type the web page name for the new data:  \n")
    data[1] = input("Type the email adress or username for the new data:  \n")
    length = int(input("Lenght of the password: \n"))
    combine = may_letters + min_letters + numbers + special_symbols 
    password = "".join(random.sample(combine, length))
    if password != '':
        success =  True
    data[2] = password
    for i in range(len(data)):
        if data[i] == "":
            print("Invalid Information")
            success = False
    return success, data