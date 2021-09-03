import sqlite3


class Database(object):
    def __init__(self):
        self.con = sqlite3.connect('inventory.db')
        self.cur = self.con.cursor()

    def __del__(self):
        self.con.close()

    def create_table(self):
        self.cur.execute("create table if not exists products(pID integer primary key, pName text,pPrice,pQty text,"
                         "pManufacturingCompany text,pContactNo text)")

    def add_new_data(self, name, price, quantity, manufacturing_company, contact):
        return self.cur.execute("INSERT INTO products (name, price, quantity, manufacturing_company, contact_no) values (?, ?, ?, ?, ?)", (name, price, quantity, manufacturing_company, contact))

    def display(self):
        return self.cur.execute("SELECT * FROM products")
