import sqlite3

class DBManager:
    def __init__(self, db_name= 'recipe_manager.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            user_id INTEGER PRIMARY KEY,
                            username TEXT NOT NULL,
                            email TEXT NOT NULL,
                            password TEXT NOT NULL
                          )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS recipes (
                            recipe_id INTEGER PRIMARY KEY,
                            recipe_name TEXT NOT NULL,
                            ingredients TEXT NOT NULL
                          )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS reviews (
                            review_id INTEGER PRIMARY KEY,
                            user_id INTEGER,
                            recipe_id INTEGER,
                            rating INTEGER,
                            comment TEXT,
                            FOREIGN KEY(user_id) REFERENCES users(user_id),
                            FOREIGN KEY(recipe_id) REFERENCES recipes(recipe_id)
                          )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS favorites (
                            favorite_id INTEGER PRIMARY KEY,
                            user_id INTEGER,
                            recipe_id INTEGER,
                            FOREIGN KEY(user_id) REFERENCES users(user_id),
                            FOREIGN KEY(recipe_id) REFERENCES recipes(recipe_id)
                          )''')
        
        self.conn.commit()

    def execute_query(self, query, params=()):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
        return cursor

    def fetch_all(self, query, params=()):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
