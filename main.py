##----------------Test Variables--------------------##
mainUser = "casijo1"
mainPwd = "Jmcr2001!@"

def main_menu():
   flag_master_data = False
   cont_intentos = 5
   while (cont_intentos > 0):
        print("Welcome to your personal Password Administrator \n")
        master_user = input("Type the Master Username: \n")
        master_password = input("Type the Master Password: \n")
        if master_password == mainPwd and master_user == mainUser:
            flag_master_data = True
            return flag_master_data
        else:
            cont_intentos-=1
            print("Error en los datos ingresados!!! \n")
            print("Intentos Restantes: ", cont_intentos)
            flag_master_data = False
    
   if cont_intentos < 1:
        print("Programa Bloqueado")
        return flag_master_data
def options_menu():
    print("----MAIN MENU---- \n")
    print("----1.Create Random Password---- \n")
    print("----2.Add New Password      ---- \n")
    print("----3.Show Password         ---- \n")
    print("----4.Update Password       ---- \n")
    print("----5.Delete Password       ---- \n")
    opc = input("Selecciona una opcion: ")
##----------------------------- Main Code ----------------------------------##
def main():
    auth_flag = False
    auth_flag = main_menu()
    if auth_flag == True:
       options_menu()

if __name__ == "__main__":
    main()