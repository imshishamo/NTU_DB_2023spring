import sqlite3


con = sqlite3.connect('platform.db')
con.execute('PRAGMA foreign_keys = ON')

def createTable():
    with con:
        cursor=con.cursor()
        
        # buyers
        cursor.execute('''CREATE TABLE IF NOT EXISTS buyers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL CHECK(length(name) <= 32),
                        gender TEXT NOT NULL CHECK(length(gender) <= 32),
                        age INTEGER,
                        phone TEXT UNIQUE NOT NULL CHECK(length(phone) <= 32),
                        email TEXT UNIQUE NOT NULL CHECK(length(email) <= 32),
                        password TEXT NOT NULL CHECK(length(password) <= 32)
        )''')
        # sellers
        cursor.execute('''CREATE TABLE IF NOT EXISTS sellers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL CHECK(length(name) <= 32),
                        gender TEXT NOT NULL CHECK(length(gender) <= 32),
                        age INTEGER,
                        phone TEXT UNIQUE NOT NULL CHECK(length(phone) <= 32),
                        email TEXT UNIQUE NOT NULL CHECK(length(email) <= 32),
                        password TEXT NOT NULL CHECK(length(password) <= 32),
                        description TEXT NOT NULL CHECK(length(password) <= 128)
        )''')
        # properties
        cursor.execute('''CREATE TABLE IF NOT EXISTS properties (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL CHECK(length(name) <= 32),
                        address TEXT NOT NULL CHECK(length(address) <= 32),
                        description TEXT NOT NULL CHECK(length(description) <= 128),
                        price INTEGER,
                        size INTEGER,
                        published_at DATETIME,
                        seller_id INTEGER,
                        FOREIGN KEY(seller_id) REFERENCES sellers(id)
        )''')
        # viewings
        cursor.execute('''CREATE TABLE IF NOT EXISTS viewings (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        buyer_id INTEGER,
                        property_id INTEGER,
                        viewed_at DATETIME,
                        rating INTEGER,
                        UNIQUE(buyer_id, viewed_at),
                        FOREIGN KEY(buyer_id) REFERENCES buyers(id),
                        FOREIGN KEY(property_id) REFERENCES properties(id)
        )''')


def addData():
    buyer_data_list = [
        {"name": "Tim", "gender": "M", "age": 30, "phone": "0987654321", "email": "tim@ntu.edu.tw", "password": "abc123"},
        {"name": "Johnson", "gender": "M", "age": 31, "phone": "0912345678", "email": "johnson@ntu.edu.tw", "password": "def456"},
        {"name": "Tina", "gender": "F", "age": 29, "phone": "0918273645", "email": "tina@ntu.edu.tw", "password": "ghi789"},
    ]

    seller_data_list = [
        {"name": "Tony", "gender": "M", "age": 35, "phone": "0981726354", "email": "tony@ntu.edu.tw", "password": "jkl123", "description": "Nice"},
        {"name": "Pochuan", "gender": "M", "age": 33, "phone": "0917823564", "email": "pochuan@ntu.edu.tw", "password": "mno456", "description": "Great"},
    ]

    properties_data_list = [
        {"name": "Sunny Lake House", "address": "767 5th Ave, New York, NY 10153", "description": "A beautiful lake house with 4 bedrooms and a large garden.", "price": 500000, "size": 350, "published_at": "2024-02-01 18:00:00", "seller_id": 1 },
        {"name": "Downtown Apartment", "address": "1 E 57th St, New York, NY 10022", "description": "Modern apartment in the heart of the city, perfect for young professionals.", "price": 300000, "size": 85, "published_at": "2024-02-05 12:00:00", "seller_id": 1 },
        {"name": "Cozy Cottage", "address": "6 E 57th St, New York, NY 10022", "description": "A quaint cottage located in the countryside, ideal for a weekend getaway.", "price": 250000, "size": 120, "published_at": "2024-03-03 15:00:00", "seller_id": 2 },
        {"name": "Mountain View Loft", "address": "545 5th Ave, New York, NY 10017", "description": "A spacious loft with stunning mountain views, featuring an open floor plan and modern amenities.", "price": 400000, "size": 250, "published_at": "2024-03-04 09:00:00", "seller_id": 2 }
    ]

    viewings_data_list = [
        {"buyer_id": 1, "property_id": 1, "viewed_at": "2024-02-05 18:00:00", "rating": 8},
        {"buyer_id": 2, "property_id": 1, "viewed_at": "2024-02-10 12:00:00", "rating": 10},
        {"buyer_id": 3, "property_id": 2, "viewed_at": "2024-03-03 18:00:00", "rating": 7},
        {"buyer_id": 1, "property_id": 3, "viewed_at": "2024-03-05 09:00:00", "rating": 6},
        {"buyer_id": 2, "property_id": 2, "viewed_at": "2024-03-06 12:00:00", "rating": 9},
        {"buyer_id": 3, "property_id": 2, "viewed_at": "2024-03-06 18:00:00", "rating": 8},
        {"buyer_id": 1, "property_id": 3, "viewed_at": "2024-03-07 09:00:00", "rating": 7},
        {"buyer_id": 2, "property_id": 2, "viewed_at": "2024-03-07 12:00:00", "rating": 5},
    ]

    with con:
        cursor = con.cursor()
        cursor.executemany("INSERT OR IGNORE INTO BUYERS (name, gender, age, phone, email, password) VALUES (:name, :gender, :age, :phone, :email, :password)", buyer_data_list)
        cursor.executemany("INSERT OR IGNORE INTO SELLERS (name, gender, age, phone, email, password, description) VALUES (:name, :gender, :age, :phone, :email, :password, :description)", seller_data_list)
        cursor.executemany("INSERT INTO PROPERTIES (name, address, description, price, size, published_at, seller_id) VALUES (:name, :address, :description, :price, :size, :published_at, :seller_id)", properties_data_list)
        cursor.executemany("INSERT OR IGNORE INTO VIEWINGS (buyer_id, property_id, viewed_at, rating) VALUES (:buyer_id, :property_id, :viewed_at, :rating)", viewings_data_list)


def queryData1():
    user = "tony@ntu.edu.tw"
    with con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM SELLERS INNER JOIN PROPERTIES ON PROPERTIES.seller_id = SELLERS.id WHERE SELLERS.email = '{}'".format(user))
        results = cursor.fetchall()
        for row in results:
            print(row)
    print("", end='\n')
    print("", end='\n')

def queryData2():
    with con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM PROPERTIES WHERE strftime('%m', published_at) = '03'")
        results = cursor.fetchall()
        for row in results:
            print(row)  
    print("", end='\n')
    print("", end='\n')

def updateData1():
    phone = "0912345678"
    with con:
        cursor = con.cursor()
        cursor.execute("UPDATE BUYERS SET name = 'Johnson Lin' WHERE phone = '{}'".format(phone))
        cursor.execute("SELECT * FROM BUYERS")
        results = cursor.fetchall()
        for row in results:
            print(row)  
    print("", end='\n')
    print("", end='\n')

def deleteData1():
    with con:
        cursor = con.cursor()
        cursor.execute("DELETE FROM PROPERTIES WHERE id = 4")
        cursor.execute("SELECT * FROM PROPERTIES")
        results = cursor.fetchall()
        for row in results:
            print(row)   
    print("", end='\n')
    print("", end='\n')

def addNewData():
    viewing = {"buyer_id": 3, "property_id": 1, "viewed_at": "2024-03-10 18:00:00", "rating": 8}
    with con:
        cursor = con.cursor()
        cursor.execute("INSERT INTO VIEWINGS (buyer_id, property_id, viewed_at, rating) VALUES(:buyer_id, :property_id, :viewed_at, :rating)", viewing) 
        cursor.execute("SELECT * FROM VIEWINGS")
        results = cursor.fetchall()
        for row in results:
            print(row) 
    print("", end='\n')
    print("", end='\n')

def queryData3():
    with con:
        cursor = con.cursor()
        cursor.execute("SELECT buyer_id, COUNT (*) AS viewing_total FROM VIEWINGS WHERE strftime('%Y-%m', viewed_at) = '2024-03' GROUP BY buyer_id ORDER BY viewing_total ASC")
        results = cursor.fetchall()
        print("User, Viewing Total")
        for row in results:
            print(row)  
    print("", end='\n')
    print("", end='\n')

def queryData4():
    with con:
        cursor = con.cursor()
        cursor.execute("SELECT seller_id, SUM(price) AS total_money FROM PROPERTIES GROUP BY seller_id ORDER BY total_money DESC")
        results = cursor.fetchall()
        print("Max User, Total Money") 
        print(results[0])
    print("", end='\n')
    print("", end='\n')

def queryData5():
    with con:
        cursor = con.cursor()
        cursor.execute("SELECT property_id, AVG(rating) AS avg_rating FROM viewings GROUP BY property_id HAVING avg_rating > 7")
        results = cursor.fetchall()
        print("Property ID, Average Rating") 
        for row in results:
            print(row) 
    print("", end='\n')
    print("", end='\n')

def queryData6():
    with con:
        cursor = con.cursor()
        cursor.execute('''SELECT PROPERTIES.seller_id, SELLERS.name, COUNT(*) AS view_most
                       FROM VIEWINGS 
                       INNER JOIN PROPERTIES ON PROPERTIES.id = VIEWINGS.property_id
                       INNER JOIN SELLERS ON PROPERTIES.seller_id = SELLERS.id
                       WHERE strftime('%Y-%m', viewed_at) = '2024-03' 
                       GROUP BY PROPERTIES.seller_id

        ''')
        results = cursor.fetchall()
        print("Seller ID, Seller Name, Viewed Count") 
        print(results[0]) 
    print("", end='\n')
    print("", end='\n')

if __name__ == '__main__':
    createTable()
    addData()
    queryData1()
    queryData2()
    updateData1()
    deleteData1()
    addNewData()
    queryData3()
    queryData4()
    queryData5()
    queryData6()
    con.commit()
    con.close()