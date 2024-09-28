import sqlite3

con = sqlite3.connect('platform2.db')
con.execute('PRAGMA foreign_keys = ON')

def createTable(): 
    with con:
        cursor=con.cursor() #cursor是一個指標 幫助在資料庫裡面
        cursor.execute('PRAGMA foreign_keys = ON')

        # price
        cursor.execute('''CREATE TABLE IF NOT EXISTS price (
                        HouseName TEXT UNIQUE NOT NULL CHECK(length(HouseName) <= 32),
                        HousePrice INTEGER,
                        SellerName TEXT UNIQUE NOT NULL CHECK(length(SellerName) <= 32) 
        )''')
        
        # buyer
        cursor.execute('''CREATE TABLE IF NOT EXISTS buyer (
                        BuyerID INTEGER,
                        BuyerName TEXT UNIQUE NOT NULL CHECK(length(BuyerName) <= 32)
        )''')
        

        # viewings
        cursor.execute('''CREATE TABLE IF NOT EXISTS viewings (
                        ViewingDate TEXT,
                        BuyerID INTEGER,
                        HouseName TEXT UNIQUE NOT NULL CHECK(length(HouseName) <= 32)
        )''')
    con.commit()


createTable()

def addData():
    price_data_list = [
        {"HouseName": "Sunny Lake House", "HousePrice": 5000000, "SellerName": "Tony"},
        {"HouseName": "Cozy Cottage", "HousePrice": 2500000, "SellerName": "Pochuan"},
        {"HouseName": "Downtown Apartment", "HousePrice": 3000000, "SellerName": "Tony"},
        {"HouseName": "Mountain View Loft", "HousePrice": 4000000, "SellerName": "Pochuan"},
    ]

    buyer_data_list = [
        {"BuyerID": 1, "BuyerName": "Tim"},
        {"BuyerID": 2, "BuyerName": "Johnson"},
        {"BuyerID": 3, "BuyerName": "Tina"},

    ]


    viewings_data_list = [
        {"ViewingDate": "03-05", "BuyerID": 1, "HouseName": "Sunny Lake House"},
        {"ViewingDate": "03-05", "BuyerID": 1, "HouseName": "Cozy Cottage"},
        {"ViewingDate": "03-06", "BuyerID": 1, "HouseName": "Sunny Lake House"},
        {"ViewingDate": "03-06", "BuyerID": 1, "HouseName": "Downtown Apartment"},
        {"ViewingDate": "03-07", "BuyerID": 2, "HouseName": "Downtown Apartment"},
        {"ViewingDate": "03-07", "BuyerID": 2, "HouseName": "Cozy Cottage"},
        {"ViewingDate": "03-08", "BuyerID": 2, "HouseName": "Sunny Lake House"},
        {"ViewingDate": "03-08", "BuyerID": 2, "HouseName": "Mountain View Loft"},
        {"ViewingDate": "03-09", "BuyerID": 3, "HouseName": "Mountain View Loft"},

    ]

    with con:
        cursor = con.cursor()
        cursor.executemany("INSERT OR IGNORE INTO PRICE (HouseName, HousePrice, SellerName) VALUES (:HouseName, :HousePrice, :SellerName)", price_data_list)
        cursor.executemany("INSERT OR IGNORE INTO BUYER (BuyerID, BuyerName) VALUES (:BuyerID, :BuyerName)", buyer_data_list)
        cursor.executemany("INSERT OR IGNORE INTO VIEWINGS (ViewingDate, BuyerID, HouseName) VALUES (:ViewingDate, :BuyerID, :HouseName)", viewings_data_list)
    con.commit()
    

addData()