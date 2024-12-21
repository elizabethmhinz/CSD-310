import mysql.connector
from tabulate import tabulate  # Importing tabulate library

line_break = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
python_mysql = mysql.connector.connect(
    user="root",
    password="",
    host="localhost",
    database="Bacchus_Winery"
)
mycursor = python_mysql.cursor()
print("Connected to MySQL Bacchus_Winery Database Successfully")
print(line_break)

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

    # Create a table format for the supplier report
    table = []
    for y in supplier_complete_report:
        table.append([y[0], y[3], y[1], y[2]])

    # Print the table
    print(tabulate(table, headers=["Delivery ID", "Supplier Name", "Expected Delivery Date", "Actual Delivery Date"], tablefmt="grid"))

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

    # Printing the sales report
    print("~~ TOTAL ORDERS OF ALL WINES ~~~~~~~~~~~~~")
    table = []
    for q in range(len(sales_tuple)):
        table.append([wine_names_formatted[q], sales_tuple[q], wine_production[q][1]])

    print(tabulate(table, headers=["Wine Name", "Orders", "Production Quantity"], tablefmt="grid"))
    print("")

    # Printing distributor orders
    print("~~ DISTRIBUTOR ORDERS ~~~~~~~~~~~~~~~~~~~~")
    table = []
    for g in wine_complete_report:
        table.append([g[3], g[2], g[0]])

    print(tabulate(table, headers=["Order ID", "Distributor", "Wine Name"], tablefmt="grid"))

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

    # Print employee hours worked
    table = []
    for y in employee_complete_report:
        hour_difference = y[2] - 2080
        day_difference = hour_difference / 8
        if hour_difference < 0:
            hour_difference = hour_difference * -1
            day_difference = day_difference * -1
            table.append([y[0], y[1], f"{hour_difference} hours less", f"{day_difference} days less"])
        else:
            table.append([y[0], y[1], f"{hour_difference} hours more", f"{day_difference} days more"])

    print(tabulate(table, headers=["Employee ID", "Employee Name", "Hours Difference", "Days Difference"], tablefmt="grid"))

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
