def addPswd():
    data = ["","",""]
    success = False
    data[0] = input("Type the web page name for the new data:  \n")
    data[1] = input("Type the email adress or username for the new data:  \n")
    data[2] = input("Type the new password for the new data:  \n")
    success = True
    for i in range(len(data)):
        if data[i] == "":
            print("Invalid Information")
            success = False
    return success, data
    