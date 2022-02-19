import sqlite3

DATABASE_FILEPATH = "database/wordlist.db"

class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_FILEPATH, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def get_random_word(self):
        query = "SELECT word FROM wordlist ORDER BY RANDOM() LIMIT 1"
        rows = self.cursor.execute(query)
        for row in rows:
            return row[0].upper()

    def validate_word(self, word):
        query = f"SELECT word FROM wordlist WHERE word='{word.upper()}'"
        rows = self.cursor.execute(query)
        for rows in rows:
            print(True)
        print(False)

    def __del__(self):
        self.conn.close()
