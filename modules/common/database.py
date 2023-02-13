import sqlite3
class Database():

    def __init__(self):
        self.connection = sqlite3.connect(r'c:\_my doc\QA Global Logic\GIT\kozubenko-qa\become_qa_auto.db')
        # self.connection = sqlite3.connect(r'c:\_my doc\QA Global Logic\GIT\kozubenko-qa' + r'become_qa_auto.db')
        # self.connection = sqlite3.connect(r'c:\_my doc\QA Global Logic\GIT\kozubenko-qa' + r'become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_product_qtn_by_id(self, product_id, qtn):
        query = f"UPDATE products SET quantity = {qtn} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qtn_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_product(self, product_id, name, description, qtn):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qtn})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()
