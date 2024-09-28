import sqlite3

con = sqlite3.connect('platform.db')
con.execute('PRAGMA foreign_keys = ON')

def createTable(): 
    with con:
        cursor=con.cursor() #cursor是一個指標 幫助在資料庫裡面
        cursor.execute('PRAGMA foreign_keys = ON')

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
        # CREATE TABLE IF NOT EXISTS properties 小寫的就是tabel的名字
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
    con.commit()
    con.close()