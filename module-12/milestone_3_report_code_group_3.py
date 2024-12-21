# MILESTONE 3 MYSQL-PYTHON CODE #

import mysql.connector
line_break = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
python_mysql = mysql.connector.connect(
	user="root",
	password="GraMoChroiJan10", 
	host="localhost",
	database="Bacchus_Winery"
)
mycursor = python_mysql.cursor()
print("Connected to MySQL Bacchus_Winery Database Successfully")
print(line_break)

#print("Wine Table :")
#mycursor.execute("SELECT * FROM Wine")
#myresult = mycursor.fetchall()
#for x in myresult:
#	print(x)
#print(line_break)

def test_reports():
	print("No test report available")

def supplier_report():
	# FORMAT : Delivery ID: (Deliveries_ID) - (Supplier_Name) had a delivery expected on (Deliveries_ExpectedDeliveryDate), which arrived at (Deliveries_ActualDeliveryDate).
	mycursor.execute("""
	SELECT Deliveries_ID, 
	Supplier_ExpectedDeliveryDate, 
	Supplier_ActualDeliveryDate,
	Supplier_Name
	FROM Deliveries 
	INNER JOIN Supplier ON Deliveries.Supplier_ID=Supplier.Supplier_ID
	""")
	supplier_complete_report = mycursor.fetchall()
	for y in supplier_complete_report:
		print("Delivery ID: {} - {} had a delivery expected on {}, which arrived at {}.".format(y[0], y[3], y[1], y[2]))

def wine_sales_report():
	mycursor.execute("""
	SELECT Wine_Name,
	Wine_ProductionQuantity,
	Order_Distributor,
	Order_ID
	FROM Wine
	LEFT JOIN Orders ON Orders.Wine_ID=Wine.Wine_ID
	""")
	wine_complete_report = mycursor.fetchall()
	# COMPILING INFORMATION ########################################################
	winemart_orders = 0
	drink_well_orders = 0
	porcelainne_orders = 0
	mcduncans_orders = 0
	for a in wine_complete_report:
		if a[2] == 'WineMart':
			winemart_orders += 1
		if a[2] == 'Drink Well':
			drink_well_orders += 1
		if a[2] == 'Porcelainne':
			porcelainne_orders += 1
		if a[2] == 'McDuncans':
			mcduncans_orders += 1
	order_tuple = (
		winemart_orders,
		drink_well_orders,
		porcelainne_orders,
		mcduncans_orders
		)
	merlot_sales = 0
	cabernet_sales = 0
	chablis_sales = 0
	chardonnay_sales = 0
	for b in wine_complete_report:
		if b[0] == 'Merlot':
			merlot_sales += 1
		if b[0] == 'Cabernet':
			cabernet_sales += 1
		if b[0] == 'Chablis':
			chablis_sales += 1
		if b[0] == 'Chardonnay':
			chardonnay_sales += 1
	sales_tuple = (
		merlot_sales,
		cabernet_sales,
		chablis_sales,
		chardonnay_sales
		)
	wine_names_formatted = ('Merlot', 'Cabernet', 'Chablis', 'Chardonnay')
	mycursor.execute("""
	SELECT Wine_Name,
	Wine_ProductionQuantity
	FROM Wine
	""")
	wine_production = mycursor.fetchall()
	# INFORMATION FETCHING OVER, NOW PRINTING ######################################
	print("~~ TOTAL ORDERS OF ALL WINES ~~~~~~~~~~~~~")
	print_counter = 0
	for q in sales_tuple:
		print(f"There were {sales_tuple[print_counter]} orders for {wine_names_formatted[print_counter]} wine in the past year, compared to the {wine_production[print_counter][1]} production quantity of this wine.")
		print_counter += 1
	print("")
	# COMPILING INFORMATION ########################################################
	print("~~ DISTRUBUTOR ORDERS ~~~~~~~~~~~~~~~~~~~~")
	print_counter = 0
	for g in wine_complete_report:
		print(f"Order ID: {g[3]} - {g[2]} purchased {g[0]}")

	

def employee_report():
	# FORMAT : Employee ID: (Employee_ID) - (Employee_Name) worked (Employee_Hours) hours during the last four quarters, 
	# where the expected hours of a full-time employee is 2080 hours. 
	mycursor.execute("""
	SELECT Employee_ID,
	Employee_Name,
	Employee_Hours
	FROM Employee
	""")
	employee_complete_report = mycursor.fetchall()
	for y in employee_complete_report:
		hour_difference = y[2] - 2080
		day_difference = hour_difference / 8
		if hour_difference < 0:
			hour_difference = hour_difference * -1
			day_difference = day_difference * -1
			print("Employee ID: {} - {} worked ".format(y[0], y[1]) + str(hour_difference) + " hours less than the expected 2,080 hours of a full-time employee. This is equivalent to " + str(day_difference) + " 8-hour business days.")
		else:
			print("Employee ID: {} - {} worked ".format(y[0], y[1]) + str(hour_difference) + " hours more than the expected 2,080 hours of a full-time employee. This is equivalent to " + str(day_difference) + " 8-hour business days.")
			#print("Employee ID: {} - {} worked {} hours during the last four quarters, where the expected hours of a full-time employee is 2080 hours.".format(y[0], y[1], y[2]))

# USER MENU
while True:
	print("Please enter the number of the report you would like to view:")
	print("1. Supplier Deliveries")
	print("2. Wine Distribution & Sales")
	print("3. Employee Hours")
	print("Otherwise, enter 'q' to quit.")
	print("")
	report_input = input(">>>")
	report_input = report_input.upper()
	if report_input == "Q":
		print("Quitting program . . .")
		print(line_break)
		break
	elif report_input == "1":
		print("Printing Supplier Deliveries Report . . .")
		supplier_report()
	elif report_input == "2":
		print("Printing Wine Distribution & Sales Report . . .")
		wine_sales_report()
	elif report_input == "3":
		print("Printing Employee Hours Report . . .")
		employee_report()
	elif report_input == "T":
		print("Printing Test Report . . .")
		test_reports()
	else:
		print("Sorry, you appeared to have input an invalid command.")
		print("Please try again.")
	print(line_break)
	print("")

