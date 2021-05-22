import sqlite3

connection = sqlite3.connect('sneaker.db')
cursor = connection.cursor()
#cursor.execute("DROP TABLE buyers")
#cursor.execute("CREATE TABLE buyers (id integer primary key AUTOINCREMENT, name text, sneaker text, size real , price real)")
buyer_record = [('Jed','Nike Kobe 5 Protro',9.5,510), ('Issac','Jordan 1 Retro High Travis Scott',12,1995), ('Greg','Nike Air Max 1/97',11,1413)]
cursor.executemany("INSERT INTO buyers VALUES (null,?,?,?,?)", buyer_record)

#cursor.execute("CREATE TABLE Kobe_5_chaos (size real, price real)")
#menu = [(3.5,399),(4,500),(4.5,765),(5,810),(5.5, 600),(6, 475),(6.5, 950),(7, 450),(7.5, 350),(8, 399),(8.5, 450),(9, 446),(9.5, 510),(10, 574),(10.5, 620),(11, 730), (11.5, 700), (12, 693), (12.5, 1171), (13, 822), (13.5, 975)]
#cursor.executemany("INSERT INTO kobe_5_chaos VALUES (?,?)", menu)

#cursor.execute("CREATE TABLE sneaker_menu (id integer primary key, sneaker text)")
#menu = [(1,'Nike Kobe 5 Protro'), (2,'Jordan 1 Retro High Travis Scott'), (3,'Nike Air Max 1/97')]
#cursor.executemany("INSERT INTO sneaker_menu VALUES (?,?)", menu)

#cursor.execute("CREATE TABLE Jordan_1_High_Travis_Scott (size real, price real)")
#record = [(4,2345),(4.5,2087),(5,2051),(5.5,2193),(6,3256),(6.5,3400),(7,2100),(7.5,1866),(8,1950),(8.5,1946),(9,1990),(9.5,1944),(10,1950),(10.5,1845),(11,1815), (11.5,1966), (12,1997), (12.5,2716), (13,2000), (14, 1650)]
#cursor.executemany("INSERT INTO Jordan_1_High_Travis_Scott VALUES (?,?)", record)

#cursor.execute("CREATE TABLE nike_air_max_sean_wotherspoon (size real, price real)")
#record = [(4,1150),(4.5,2059),(5,1472),(5.5,1375),(6,1169),(6.5,1242),(7,1243),(7.5,1219),(8,1150),(8.5,1250),(9,1258),(9.5,1300),(10,1300),(10.5,1335),(11,1413), (11.5,1545), (12,1675), (12.5,2000), (13,1577), (14, 3000)]
#cursor.executemany("INSERT INTO nike_air_max_sean_wotherspoon VALUES (?,?)", record)


def display_buyer_order():
    cursor.execute("SELECT * FROM buyers")
    print("{:<10}  {:<10}  {:<35}  {:<10}  {:<10} ".format("Buyer ID", "Name", "Sneaker", "Size", "Price"))
    for record in cursor.fetchall():
        print("{:<10}  {:<10}  {:<35}  {:<10}  {:<10}".format(record[0],record[1],record[2],record[3],record[4]))

def display_menu():
    cursor.execute("SELECT * FROM sneaker_menu")
    print("{:<10}  {:<10}".format("Sneaker ID", "Sneaker"))
    for record in cursor.fetchall():
        print("{:<10}  {:<10}".format(record[0],record[1]))

def display_kobe_5_chaos():
    cursor.execute("SELECT * FROM kobe_5_chaos")
    print("{:<10}  {:<10}".format("Size", "Price"))
    for record in cursor.fetchall():
        print("{:<10}  {:<10}".format(record[0],record[1]))

def display_jordan_1_high_travis_scott():
    cursor.execute("SELECT * FROM Jordan_1_High_Travis_Scott")
    print("{:<10}  {:<10}".format("Size", "Price"))
    for record in cursor.fetchall():
        print("{:<10}  {:<10}".format(record[0],record[1]))

def display_nike_air_max_sean_wotherspoon():
    cursor.execute("SELECT * FROM nike_air_max_sean_wotherspoon")
    print("{:<10}  {:<10}".format("Size", "Price"))
    for record in cursor.fetchall():
        print("{:<10}  {:<10}".format(record[0],record[1]))                


choice = None
while choice != "7":
    print("1) Add Order")
    print("2) Update Order")
    print("3) Delete Order")
    print("4) Print all Orders")
    print("5) Print menu")
    print("6) Search")
    print("7) Quit")
    choice = input("> ")
    print()
    if choice == "1":
        # Add New Order
        name = input("Buyer name: ")
        sneaker = input("Sneaker: ")
        size = float(input("Size: "))
        price = float(input("Price: "))
        values = (name, sneaker, size, price)
        cursor.execute("INSERT INTO buyers (name, sneaker, size, price) VALUES (?,?,?,?)", values)
        connection.commit()
        print()

    elif choice == "2":
        # Upate order
        name = input("Name: ")
        sneaker = input("Sneaker: ")
        size = float(input("Size: "))
        price = float(input("Price: "))
        values = (sneaker, size, price, name)
        cursor.execute("UPDATE buyers SET sneaker = ?, size = ?, price = ? WHERE name = ?", values)
        connection.commit()
        print()

    elif choice == "3":
        # Delete order
        name = input("Name: ")
        sneaker = input("Sneaker: ")
        values = (name, sneaker )
        cursor.execute("DELETE FROM buyers WHERE name = ? AND sneaker = ?", values)
        connection.commit()
        print()

    elif choice == "4":
        # Display orders
        display_buyer_order()
        print()

    elif choice =="5":
        #Display menu
        display_menu()
        print()

    elif choice =="6":
        want_search = True
        while want_search == True:
            search = input("> ")
            if search.lower() == "kobe 5 chaos":
                display_kobe_5_chaos()
                print()

            elif search.lower() == "jordan 1 high travis scott":
                display_jordan_1_high_travis_scott()
                print()

            elif search.lower() == "nike air max 1/97":
                display_nike_air_max_sean_wotherspoon()
                print()  

            elif search.lower() == "b":
                want_search = False
                print()    



connection.close()