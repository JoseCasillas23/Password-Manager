# Password Manager 
### Step 1: Choose Programming Language
* Python: Es el lenguaje elegido porque cuenta con todas las funcionalidades necesarias para los siguientes pasos
### Step 2: Program Flow
* The flow of the program to insert a row will be:
1. Capturing the initial data
2. Encrypt the introduced data -> https://shre.ink/rsAF
3. Serialize the data -> https://www.solvetic.com/tutoriales/article/2920-como-serializar-y-deserializar-datos-en-python/
4. Store in the DB
5. Upload to the Cloud
To pull some data will be:
1. Download from the Cloud or DB
2. Deserialize the data
3. Decipher the data
3. Show the data 
### Step 3: GUI
* Search for a Extension to work with Python and a GUI 
* Options for a GUI = https://realpython.com/pysimplegui-python/
### Connection Python with MySQL
* First of all I must create a new DB in the MySQL system with my previous info
* Second I need to create a table with the following columns: username, platform, password 
* Finally the connection between my DB an my app created using the following link: https://shre.ink/rs5f

### Connect the DB with the Cloud
* For more information consult the following link https://shre.ink/rsAv

### Planing Stage 3:
1. Design and deliver a prototype of the GUI.
2. Create a main script with the following features:
   *  Step 1: Ask the user for a main username and password
   *  Step 2: Open a main menu with the options: Generate, Insert, Show, Delete, Update passwords
   *  Generate Op: Ranmly creates a password with: caps, len = 8-20, special characters, numbers
   *  Insert Op: Gives you three fields to be filled: username, password, platform
   *  Show Op: Allows you to show all your passwords or search for one in specific
   *  Delete: Searchs for a password and delete the data, add some confirmation field
   *  Update: Searhc for a password and update the data, add some confirmation field
3. Find a way to to create the tables needed for the software one time only 
4. Connect the main script with MySQL to storage all the important data
5. Verification check to be sure al CRUD operations are performed in the DataBase
### Planning Stage 4:
1. Add encryption and serialization methods
3. Incorporate the GUI with the main script
4. Apply design patterns and software architecture
5. Implement cybersecurity measures within the Data Base
6. Run some testing scenarios in corner cases
7. Use AWS to store the information 
