import sqlite3

def create_table_cars():
        connection = sqlite3.connect("Data_access/cars_db.db")
        cursor = connection.cursor()
        cursor.execute("create table persons (id integer primary key  autoincrement, name text, model text, plate text, color text)")
        connection.commit()
        connection.close()


def save_cars(name,model,plate,color):
        connection = sqlite3.connect("data_access/cars_db.db")
        cursor = connection.cursor()
        cursor.execute("insert into persons (name ,model,plate,color) values(?,?,?,?)",
                    [name, model, plate, color])
        connection.commit()
        connection.close()