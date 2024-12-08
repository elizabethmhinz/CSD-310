# TRUMAN MILESTONE 2 MYSQL-PYTHON CODE #

import mysql.connector
from mysql.connector import errorcode
line_break = "~~~~~~~~~~~~~~~~~~~~~"

python_mysql = mysql.connector.connect(
	user="root",
	password="YourRootPassword", 
	host="localhost"
)
mycursor = python_mysql.cursor()
print("Connected to MySQL Successfully")
print(line_break)

# Added line to skip creating database if it already exists 
mycursor.execute("CREATE DATABASE IF NOT EXISTS Bacchus_Winery")
print("Bacchus_Winery Database Created Successfully")
print(line_break)

print("Re-Connecting to MySQL Using New Database")
python_mysql = mysql.connector.connect(
	user="root",
	password="YourRootPassword", 
	host="localhost",
	database="Bacchus_Winery"
)
mycursor = python_mysql.cursor()
print("Connected to MySQL Bacchus_Winery Database Successfully")
print(line_break)

# Added code to skip creating table if it already exists
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Department (
        Department_ID INT AUTO_INCREMENT,
        Department_Name VARCHAR(99),
        PRIMARY KEY (Department_ID)
    );
""")
# Added line to show if table was successful 
print("Department Table Created Successfully")
print(line_break)

mycursor.execute("""
	INSERT INTO Department (Department_Name)
	VALUES 
		("Owner"),
		("Finances"),
		("Marketing"), 
		("Production Line"), 
		("Distribution"),
		("Harvesting");
""")
# Added line to show if records inserted were successful
print("Department Records Inserted Successfully")
print(line_break)

#mycursor.execute("SELECT * FROM Department")
#myresult = mycursor.fetchall()
#for x in myresult:
#	print(x)

# Added code to skip creating table if it already exists
mycursor.execute("""
	CREATE TABLE IF NOT EXISTS Supervisor (
		Supervisor_ID INT NOT NULL AUTO_INCREMENT,
		Supervisor_Name varchar(99),
		Department_ID INT,
		PRIMARY KEY (Supervisor_ID),
		FOREIGN KEY (Department_ID)REFERENCES Department(Department_ID)
);
""")
print("Supervisor Table Created Successfully")
print(line_break)

mycursor.execute("""
	INSERT INTO Supervisor (Supervisor_Name, Department_ID)
	VALUES 
		("Stan Bacchus",(SELECT Department_ID FROM Department WHERE Department_Name = "Owner")),
		("Davis Bacchus",(SELECT Department_ID FROM Department WHERE Department_Name = "Owner")),
		("Janet Collins",(SELECT Department_ID FROM Department WHERE Department_Name = "Finances")),
		("Roz Murphy",(SELECT Department_ID FROM Department WHERE Department_Name = "Marketing")),
		("Henry Doyle",(SELECT Department_ID FROM Department WHERE Department_Name = "Production Line")),
		("Maria Costanza",(SELECT Department_ID FROM Department WHERE Department_Name = "Distribution"));
""")
# Added line to show if supervisor records insert was successful
print("Supervisor Records Inserted Successfully")
print(line_break)

# Added line to not create table if it already exists 
mycursor.execute("""
	CREATE TABLE IF NOT EXISTS Employee (
		Employee_ID INT AUTO_INCREMENT,
		Employee_Name varchar(99),
		Department_ID INT,
		Supervisor_ID INT,
		PRIMARY KEY (Employee_ID),
		FOREIGN KEY (Department_ID)REFERENCES Department(Department_ID),
		FOREIGN KEY (Supervisor_ID)REFERENCES Supervisor(Supervisor_ID)
    );
""")

mycursor.execute("""
	INSERT INTO Employee (Employee_Name, Department_ID, Supervisor_ID)
	VALUES 
		("Bob Ulrich",(SELECT Department_ID FROM Department WHERE Department_Name = "Marketing"),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = "Roz Murphy")),
		("Kristina Lee",(SELECT Department_ID FROM Department WHERE Department_Name = "Distribution"),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = "Maria Costanza")),
		("Timothy Thomas",(SELECT Department_ID FROM Department WHERE Department_Name = "Production Line"),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = "Henry Doyle")),
		("Samuel James",(SELECT Department_ID FROM Department WHERE Department_Name = "Production Line"),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = "Henry Doyle")),
		("Natalie Pops",(SELECT Department_ID FROM Department WHERE Department_Name = "Production Line"),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = "Henry Doyle")),
		("Wilson Wilson",(SELECT Department_ID FROM Department WHERE Department_Name = "Production Line"),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = "Henry Doyle")),
		("Ryan Carlson",(SELECT Department_ID FROM Department WHERE Department_Name = "Production Line"),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = "Henry Doyle")),
		("Carlos Aguilar",(SELECT Department_ID FROM Department WHERE Department_Name = "Production Line"),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = "Henry Doyle")),
		("Kari Lake",(SELECT Department_ID FROM Department WHERE Department_Name = "Production Line"),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = "Henry Doyle")),
		("Owain Martins",(SELECT Department_ID FROM Department WHERE Department_Name = "Production Line"),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = "Henry Doyle")),
		("Cynthia Black",(SELECT Department_ID FROM Department WHERE Department_Name = "Harvesting"),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = "Henry Doyle")),
		("Brendan Gray",(SELECT Department_ID FROM Department WHERE Department_Name = "Production Line"),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = "Henry Doyle")),
		("Erin Young",(SELECT Department_ID FROM Department WHERE Department_Name = "Harvesting"),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = "Henry Doyle")),
		("Donald Rich",(SELECT Department_ID FROM Department WHERE Department_Name = "Harvesting"),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = "Henry Doyle")),
		("Joy Loomis",(SELECT Department_ID FROM Department WHERE Department_Name = "Harvesting"),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = "Henry Doyle")),
		("Fred West",(SELECT Department_ID FROM Department WHERE Department_Name = "Harvesting"),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = "Henry Doyle")),
		("Zac Oyama",(SELECT Department_ID FROM Department WHERE Department_Name = "Harvesting"),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = "Henry Doyle")),
		("Olive Mendez",(SELECT Department_ID FROM Department WHERE Department_Name = "Harvesting"),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = "Henry Doyle")),
		("George Novacs",(SELECT Department_ID FROM Department WHERE Department_Name = "Production Line"),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = "Henry Doyle")),
		("Patrick Hackett",(SELECT Department_ID FROM Department WHERE Department_Name = "Production Line"),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = "Henry Doyle")),
		("Doug Dawson",(SELECT Department_ID FROM Department WHERE Department_Name = "Production Line"),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = "Henry Doyle")),
		("Leon Yarrows",(SELECT Department_ID FROM Department WHERE Department_Name = "Production Line"),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = "Henry Doyle"));
""")
print("Employee Records Inserted Successfully")
print(line_break)

# Added code to commit changes and close connection
python_mysql.commit()
mycursor.close()
python_mysql.close()