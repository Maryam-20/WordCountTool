import mysql.connector as sql
import csv

class Stock:
    
    def __init__(self):
        self.mydb = sql.connect (
            host = "localhost",
            user = "root",
            password = "",
            database = "stockPrice_db"
        )
        self.mycursor = self.mydb.cursor()
        # self.mycursor.execute("CREATE DATABASE stockPrice_db")
        # self.mycursor.execute("CREATE TABLE StockDetails (COLUMN_ID INT AUTO_INCREMENT PRIMARY KEY, DATE VARCHAR(30), OPEN VARCHAR(20), HIGH VARCHAR(20), LOW VARCHAR(20), CLOSE VARCHAR(20), ADJCLOSE VARCHAR(20), VOLUME VARCHAR(20))")
        self.file_csv()

    def file_csv(self):
        with open("C:\\Users\\Hp\\Documents\\stock_price.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                date, open_val, high, low, close, adjclose, volume = row
                 
                query = "INSERT INTO StockDetails (DATE, OPEN, HIGH, LOW, CLOSE, ADJCLOSE, VOLUME) VALUES  (%s, %s, %s, %s, %s, %s, %s)"
                val = (date, open_val, high, low, close, adjclose, volume)
                self.mycursor.execute(query, val)
                self.mydb.commit() 
                print("data inserted succesfully")
                # print(",".join(row))
  
st = Stock()
