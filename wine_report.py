import mysql.connector

# Connect to the database
python_mysql = mysql.connector.connect(
    user="root",
    password="YourRootPassword", 
    host="localhost",
    database="Bacchus_Winery"
)
mycursor = python_mysql.cursor()

# Line break for better output readability
line_break = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

def generate_report():
    print("Wine Distribution Report")
    print(line_break)

    # Query 1: Are all wines selling as they thought?
    print("1. Are all wines selling as expected?")
    mycursor.execute("""
        SELECT Wine.Wine_Name, COUNT(Orders.Order_ID) AS Total_Orders, Wine.Wine_ProductionQuantity
        FROM Wine
        LEFT JOIN Orders ON Wine.Wine_ID = Orders.Wine_ID
        GROUP BY Wine.Wine_ID;
    """)
    results = mycursor.fetchall()
    for wine_name, total_order in results:
        status = "Yes" if total_orders >= 5 else "No"
        print(f"- {wine_name}: Orders = {total_orders}, Production Quantity = {production_quantity}, Selling as Expected = {status}")
    print(line_break)

    # Query 2: Is one wine not selling?
    print("2. Is any wine not selling?")
    mycursor.execute("""
        SELECT Wine.Wine_Name
        FROM Wine
        LEFT JOIN Orders ON Wine.Wine_ID = Orders.Wine_ID
        WHERE Orders.Order_ID IS NULL;
    """)
    results = mycursor.fetchall()
    if results:
        for wine_name, in results:
            print(f"- {wine_name} is not selling.")
    else:
        print("- All wines are selling.")
    print(line_break)

    # Query 3: Which distributor carries which wine?
    print("3. Which distributor carries which wine?")
    mycursor.execute("""
        SELECT DISTINCT Orders.Order_Distributor, Wine.Wine_Name
        FROM Orders
        JOIN Wine ON Orders.Wine_ID = Wine.Wine_ID
        ORDER BY Orders.Order_Distributor, Wine.Wine_Name;
    """)
    results = mycursor.fetchall()
    current_distributor = None
    for distributor, wine_name in results:
        if distributor != current_distributor:
            if current_distributor is not None:
                print()  # Newline for a new distributor
            print(f"Distributor: {distributor}")
            current_distributor = distributor
        print(f"  - {wine_name}")

    print(line_break)

# Run the report
generate_report()

# Close the connection
mycursor.close()
python_mysql.close()
