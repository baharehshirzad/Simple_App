import sqlite3
from datetime import datetime


def create_table_cars():
        connection = sqlite3.connect("data_access/cars_db.db")
        cursor = connection.cursor()
        cursor.execute("create table cars (id integer primary key  autoincrement, name text, model text, plate text, color text,date_time text)")
        connection.commit()
        connection.close()



def save_cars(name,model,plate,color):
        connection = sqlite3.connect("cars_db.db")
        cursor = connection.cursor()
        cursor.execute("insert into cars(name ,model,plate,color,date_time) values(name, model, plate, color)",
                       [name,model,plate,color,datetime.now()])
        connection.commit()
        connection.close()

