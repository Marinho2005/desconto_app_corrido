import sqlite3

class DBConnection:
    def __init__(self, db_name: str = "database.db"):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

    def get_connection(self):
        return sqlite3.connect(self.db_name)

