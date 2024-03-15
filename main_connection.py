# - Use the pip command to install MySQL connector Python
# pip install mysql-connector-python
import mysql.connector 

#https://pynative.com/python-mysql-database-connection/#:~:text=How%20to%20Connect%20to%20MySQL%20Database%20in%20Python,module%E2%80%99s%20methods%20to%20communicate%20with%20the%20MySQL%20database

try: 
    """
    Reemplazar:
    database = 'nombre de la base de datos en donde se guarda todo'
    user = 'nombre del usuario que maneja las bases de datos en mi compu'
    password = 'contra del usuario'
    """
    #Ingresar un if para que esta accion solo se haga una vez 
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29')
    
    mySql_Create_Table_Query = """CREATE TABLE mainInfo (
                             Id int(11) NOT NULL,
                             Web_Page varchar(250) NOT NULL,
                             Username varchar(60) NOT NULL,
                             Password varchar(60) NOT NULL,
                             Add_Date Date NOT NULL,
                             PRIMARY KEY (Id)) """
    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("mainInfo Table created successfully ")
    
except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")