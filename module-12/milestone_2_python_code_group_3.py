# MILESTONE 2 MYSQL-PYTHON CODE #

import mysql.connector
#from mysql.connector import errorcode
line_break = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

python_mysql = mysql.connector.connect(
	user="root",
	password="", 
	host="localhost"
)
mycursor = python_mysql.cursor()
print("Connected to MySQL Successfully")
print(line_break)

mycursor.execute("DROP DATABASE IF EXISTS Bacchus_Winery;")
mycursor.execute("CREATE DATABASE Bacchus_Winery")
print("Bacchus_Winery Database Created Successfully")
print(line_break)

print("Re-Connecting to MySQL Using New Database")
python_mysql = mysql.connector.connect(
	user="root",
	password="", 
	host="localhost",
	database="Bacchus_Winery"
)
mycursor = python_mysql.cursor()
print("Connected to MySQL Bacchus_Winery Database Successfully")
print(line_break)

mycursor.execute("DROP TABLE IF EXISTS Department;")
mycursor.execute("DROP TABLE IF EXISTS Supervisor;")
mycursor.execute("DROP TABLE IF EXISTS Employee;")
mycursor.execute("DROP TABLE IF EXISTS Wine;")
mycursor.execute("DROP TABLE IF EXISTS Orders;")
mycursor.execute("DROP TABLE IF EXISTS Supplier;")
mycursor.execute("DROP TABLE IF EXISTS Deliveries;")
mycursor.execute("DROP TABLE IF EXISTS Inventory;")

mycursor.execute("CREATE TABLE Department (Department_ID INT NOT NULL AUTO_INCREMENT, Department_Name varchar(99), PRIMARY KEY (Department_ID));")
mycursor.execute("INSERT INTO Department (Department_Name) VALUES ('Owners'),('Finances'),('Marketing'),('Distribution'),('Production Line'),('Harvesting');")

print("Department Table :")
mycursor.execute("SELECT * FROM Department")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
print(line_break)

mycursor.execute("CREATE TABLE Supervisor (Supervisor_ID INT NOT NULL AUTO_INCREMENT,Supervisor_Name varchar(99),Department_ID int,PRIMARY KEY (Supervisor_ID),FOREIGN KEY (Department_ID)REFERENCES Department(Department_ID));")
mycursor.execute("INSERT INTO Supervisor (Supervisor_Name, Department_ID) VALUES ('Stan Bacchus',(SELECT Department_ID FROM Department WHERE Department_Name = 'Owner')),('Davis Bacchus',(SELECT Department_ID FROM Department WHERE Department_Name = 'Owner')),('Janet Collins',(SELECT Department_ID FROM Department WHERE Department_Name = 'Finances')),('Roz Murphy',(SELECT Department_ID FROM Department WHERE Department_Name = 'Marketing')),('Henry Doyle',(SELECT Department_ID FROM Department WHERE Department_Name = 'Production Line')),('Maria Costanza',(SELECT Department_ID FROM Department WHERE Department_Name = 'Distribution'));")

print("Supervisor Table :")
mycursor.execute("SELECT * FROM Supervisor")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
print(line_break)

mycursor.execute("CREATE TABLE Employee (Employee_ID INT NOT NULL AUTO_INCREMENT, Employee_Name varchar(99), Department_ID INT, Supervisor_ID INT, Employee_Hours INT, PRIMARY KEY (Employee_ID), FOREIGN KEY (Department_ID) REFERENCES Department(Department_ID), FOREIGN KEY (Supervisor_ID) REFERENCES Supervisor(Supervisor_ID));")
mycursor.execute("INSERT INTO Employee (Employee_Name, Department_ID, Supervisor_ID, Employee_Hours) VALUES ('Bob Ulrich',(SELECT Department_ID FROM Department WHERE Department_Name = 'Marketing'),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = 'Roz Murphy'), '2079'),('Kristina Lee',(SELECT Department_ID FROM Department WHERE Department_Name = 'Distribution'),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = 'Maria Costanza'), '2112'),('Timothy Thomas',(SELECT Department_ID FROM Department WHERE Department_Name = 'Production Line'),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = 'Henry Doyle'), '1992'),('Samuel James',(SELECT Department_ID FROM Department WHERE Department_Name = 'Production Line'),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = 'Henry Doyle'), '2084'),('Natalie Pops',(SELECT Department_ID FROM Department WHERE Department_Name = 'Production Line'),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = 'Henry Doyle'), '2061'),('Wilson Wilson',(SELECT Department_ID FROM Department WHERE Department_Name = 'Production Line'),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = 'Henry Doyle'), '2101'),('Ryan Carlson',(SELECT Department_ID FROM Department WHERE Department_Name = 'Production Line'),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = 'Henry Doyle'), '2048'),('Carlos Aguilar',(SELECT Department_ID FROM Department WHERE Department_Name = 'Production Line'),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = 'Henry Doyle'), '2205'),('Kari Lake',(SELECT Department_ID FROM Department WHERE Department_Name = 'Production Line'),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = 'Henry Doyle'), '2081'),('Owain Martins',(SELECT Department_ID FROM Department WHERE Department_Name = 'Production Line'),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = 'Henry Doyle'), '2078'),('Cynthia Black',(SELECT Department_ID FROM Department WHERE Department_Name = 'Harvesting'),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = 'Henry Doyle'), '1945'),('Brendan Gray',(SELECT Department_ID FROM Department WHERE Department_Name = 'Production Line'),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = 'Henry Doyle'), '2156'),('Erin Young',(SELECT Department_ID FROM Department WHERE Department_Name = 'Harvesting'),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = 'Henry Doyle'), '2007'),('Donald Rich',(SELECT Department_ID FROM Department WHERE Department_Name = 'Harvesting'),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = 'Henry Doyle'), '2041'),('Joy Loomis',(SELECT Department_ID FROM Department WHERE Department_Name = 'Harvesting'),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = 'Henry Doyle'), '2126'),('Fred West',(SELECT Department_ID FROM Department WHERE Department_Name = 'Harvesting'),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = 'Henry Doyle'), '1894'),('Zac Oyama',(SELECT Department_ID FROM Department WHERE Department_Name = 'Harvesting'),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = 'Henry Doyle'), '2088'),('Olive Mendez',(SELECT Department_ID FROM Department WHERE Department_Name = 'Harvesting'),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = 'Henry Doyle'), '2095'),('George Novacs',(SELECT Department_ID FROM Department WHERE Department_Name = 'Production Line'),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = 'Henry Doyle'), '2094'),('Patrick Hackett',(SELECT Department_ID FROM Department WHERE Department_Name = 'Production Line'),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = 'Henry Doyle'), '2086'),('Doug Dawson',(SELECT Department_ID FROM Department WHERE Department_Name = 'Production Line'),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = 'Henry Doyle'), '2071'),('Leon Yarrows',(SELECT Department_ID FROM Department WHERE Department_Name = 'Production Line'),(SELECT Supervisor_ID FROM Supervisor WHERE Supervisor_Name = 'Henry Doyle'), '2018');")

print("Employee Table :")
mycursor.execute("SELECT * FROM Employee")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
print(line_break)

mycursor.execute("CREATE TABLE Wine (Wine_ID INT NOT NULL AUTO_INCREMENT, Wine_Name varchar(99), Wine_ProductionCost INT, Wine_SellingPrice INT, Wine_ProductionQuantity INT, PRIMARY KEY (Wine_ID));")
mycursor.execute("INSERT INTO Wine (Wine_Name, Wine_ProductionCost, Wine_SellingPrice, Wine_ProductionQuantity) VALUES ('Merlot','2000','5200', '5'),('Cabernet','1250','3500','8'),('Chablis','990','2900','5'),('Chardonnay','1500','4200','4');")

print("Wine Table :")
mycursor.execute("SELECT * FROM Wine")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
print(line_break)

mycursor.execute("CREATE TABLE Orders (Order_ID INT NOT NULL AUTO_INCREMENT, Employee_ID INT, Wine_ID INT, Order_Distributor varchar(99), Order_ShipDate varchar(10), Order_DeliveryDate varchar(10), PRIMARY KEY (Order_ID), FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID), FOREIGN KEY (Wine_ID) REFERENCES Wine(Wine_ID));")
mycursor.execute("INSERT INTO Orders (Employee_ID, Wine_ID, Order_Distributor, Order_Shipdate, Order_DeliveryDate) VALUES ((SELECT Employee_ID FROM Employee WHERE Employee_Name = 'Kristina Lee'), (SELECT Wine_ID FROM Wine WHERE Wine_Name = 'Chardonnay'), 'WineMart', '01-01-2024', '01-26-2024'),((SELECT Employee_ID FROM Employee WHERE Employee_Name = 'Kristina Lee'), (SELECT Wine_ID FROM Wine WHERE Wine_Name = 'Merlot'), 'WineMart', '02-01-2024', '02-17-2024'),((SELECT Employee_ID FROM Employee WHERE Employee_Name = 'Kristina Lee'), (SELECT Wine_ID FROM Wine WHERE Wine_Name = 'Merlot'), 'Drink Well', '03-13-2024', '03-25-2024'),((SELECT Employee_ID FROM Employee WHERE Employee_Name = 'Kristina Lee'), (SELECT Wine_ID FROM Wine WHERE Wine_Name = 'Chardonnay'), 'WineMart', '04-26-2024', '05-01-2024'),((SELECT Employee_ID FROM Employee WHERE Employee_Name = 'Kristina Lee'), (SELECT Wine_ID FROM Wine WHERE Wine_Name = 'Chablis'), 'McDuncans', '04-29-2024', '05-06-2024'),((SELECT Employee_ID FROM Employee WHERE Employee_Name = 'Kristina Lee'), (SELECT Wine_ID FROM Wine WHERE Wine_Name = 'Merlot'), 'Drink Well', '05-12-2024', '05-27-2024'),((SELECT Employee_ID FROM Employee WHERE Employee_Name = 'Kristina Lee'), (SELECT Wine_ID FROM Wine WHERE Wine_Name = 'Cabernet'), 'WineMart', '05-20-2024', '05-25-2024'),((SELECT Employee_ID FROM Employee WHERE Employee_Name = 'Kristina Lee'), (SELECT Wine_ID FROM Wine WHERE Wine_Name = 'Chardonnay'), 'McDuncans', '05-30-2024', '06-03-2024'),((SELECT Employee_ID FROM Employee WHERE Employee_Name = 'Kristina Lee'), (SELECT Wine_ID FROM Wine WHERE Wine_Name = 'Chardonnay'), 'WineMart', '06-11-2024', '06-18-2024'),((SELECT Employee_ID FROM Employee WHERE Employee_Name = 'Kristina Lee'), (SELECT Wine_ID FROM Wine WHERE Wine_Name = 'Merlot'), 'Drink Well', '07-14-2024', '07-22-2024'),((SELECT Employee_ID FROM Employee WHERE Employee_Name = 'Kristina Lee'), (SELECT Wine_ID FROM Wine WHERE Wine_Name = 'Cabernet'), 'Drink Well', '08-20-2024', '08-29-2024'),((SELECT Employee_ID FROM Employee WHERE Employee_Name = 'Kristina Lee'), (SELECT Wine_ID FROM Wine WHERE Wine_Name = 'Merlot'), 'WineMart', '09-03-2024', '09-09-2024'),((SELECT Employee_ID FROM Employee WHERE Employee_Name = 'Kristina Lee'), (SELECT Wine_ID FROM Wine WHERE Wine_Name = 'Merlot'), 'WineMart', '09-12-2024', '09-22-2024'),((SELECT Employee_ID FROM Employee WHERE Employee_Name = 'Kristina Lee'), (SELECT Wine_ID FROM Wine WHERE Wine_Name = 'Merlot'), 'Porcelainne', '10-18-2024', '11-01-2024'),((SELECT Employee_ID FROM Employee WHERE Employee_Name = 'Kristina Lee'), (SELECT Wine_ID FROM Wine WHERE Wine_Name = 'Chablis'), 'Drink Well', '11-09-2024', '11-30-2024'),((SELECT Employee_ID FROM Employee WHERE Employee_Name = 'Kristina Lee'), (SELECT Wine_ID FROM Wine WHERE Wine_Name = 'Chardonnay'), 'WineMart', '12-04-2024', NULL);")

print("Orders Table :")
mycursor.execute("SELECT * FROM Orders")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
print(line_break)

mycursor.execute("CREATE TABLE Supplier (Supplier_ID INT NOT NULL AUTO_INCREMENT,Supplier_Name varchar(99),Supplier_PhoneNO varchar(10),PRIMARY KEY (Supplier_ID));")
mycursor.execute("INSERT INTO Supplier (Supplier_Name, Supplier_PhoneNO) VALUES ('Bottles & Corks Incorporated','4028886543'),('Labels & Boxes Limited','4023334444'),('Vats & Tubing Incorporated', '9091116654');")

print("Supplier Table :")
mycursor.execute("SELECT * FROM Supplier")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
print(line_break)

mycursor.execute("CREATE TABLE Inventory (Inventory_ID INT NOT NULL AUTO_INCREMENT,Inventory_Description varchar(99),Inventory_Quantity INT,Supplier_ID INT,Wine_ID INT,PRIMARY KEY (Inventory_ID),FOREIGN KEY (Supplier_ID) REFERENCES Supplier(Supplier_ID),FOREIGN KEY (Wine_ID) REFERENCES Wine(Wine_ID));")
mycursor.execute("INSERT INTO Inventory (Inventory_Description, Inventory_Quantity, Supplier_ID, Wine_ID) VALUES ('Merlot Wine', '102', NULL, (SELECT Wine_ID FROM Wine WHERE Wine_Name = 'Merlot')),('Cabernet Wine', '98', NULL, (SELECT Wine_ID FROM Wine WHERE Wine_Name = 'Cabernet')),('Chablis Wine', '326', NULL, (SELECT Wine_ID FROM Wine WHERE Wine_Name = 'Chablis')),('Chardonnay Wine', '37', NULL, (SELECT Wine_ID FROM Wine WHERE Wine_Name = 'Chardonnay')),('Bottles', '406', (SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Bottles & Corks Incorporated'), NULL),('Corks', '539', (SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Bottles & Corks Incorporated'), NULL),('Labels', '438', (SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Labels & Boxes Limited'), NULL),('Boxes', '276', (SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Labels & Boxes Limited'), NULL),('Vats', '58', (SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Vats & Tubing Incorporated'), NULL),('Tubing', '741', (SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Vats & Tubing Incorporated'), NULL);")

print("Inventory Table :")
mycursor.execute("SELECT * FROM Inventory")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
print(line_break)

mycursor.execute("CREATE TABLE Deliveries (Deliveries_ID INT NOT NULL AUTO_INCREMENT,Supplier_ID INT,Supplier_ExpectedDeliveryDate varchar(10),Supplier_ActualDeliveryDate varchar(10),PRIMARY KEY (Deliveries_ID),FOREIGN KEY (Supplier_ID) REFERENCES Supplier(Supplier_ID));")
mycursor.execute("INSERT INTO Deliveries (Supplier_ID, Supplier_ExpectedDeliveryDate, Supplier_ActualDeliveryDate) VALUES ((SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Bottles & Corks Incorporated'),'05-01-2024','05-12-2024'),((SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Bottles & Corks Incorporated'),'06-01-2024','06-03-2024'),((SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Bottles & Corks Incorporated'),'07-01-2024','07-21-2024'),((SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Bottles & Corks Incorporated'),'08-01-2024','08-16-2024'),((SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Bottles & Corks Incorporated'),'09-01-2024','09-08-2024'),((SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Bottles & Corks Incorporated'),'10-01-2024','10-06-2024'),((SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Bottles & Corks Incorporated'),'11-01-2024','11-11-2024'),((SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Labels & Boxes Limited'),'05-01-2024','05-02-2024'),((SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Labels & Boxes Limited'),'06-01-2024','06-03-2024'),((SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Labels & Boxes Limited'),'07-01-2024','07-01-2024'),((SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Labels & Boxes Limited'),'08-01-2024','08-04-2024'),((SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Labels & Boxes Limited'),'09-01-2024','09-09-2024'),((SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Labels & Boxes Limited'),'10-01-2024','10-01-2024'),((SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Labels & Boxes Limited'),'11-01-2024','11-02-2024'),((SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Vats & Tubing Incorporated'),'05-01-2024','05-09-2024'),((SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Vats & Tubing Incorporated'),'06-01-2024','06-08-2024'),((SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Vats & Tubing Incorporated'),'07-01-2024','07-06-2024'),((SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Vats & Tubing Incorporated'),'08-01-2024','08-10-2024'),((SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Vats & Tubing Incorporated'),'09-01-2024','09-08-2024'),((SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Vats & Tubing Incorporated'),'10-01-2024','10-07-2024'),((SELECT Supplier_ID FROM Supplier WHERE Supplier_Name = 'Vats & Tubing Incorporated'),'11-01-2024','11-06-2024');")

print("Deliveries Table :")
mycursor.execute("SELECT * FROM Deliveries")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
print(line_break)

python_mysql.commit()
print("All executions performed successfully.")

#mycursor.execute("CREATE TABLE ")
#mycursor.execute("INSERT INTO ")
#
#mycursor.execute("SELECT * FROM ")
#myresult = mycursor.fetchall()
#for x in myresult:
#	print(x)
#print(line_break)









