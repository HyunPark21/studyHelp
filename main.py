import psycopg2

class Database:
    def __init__(self):
        self.db = psycopg2.connect(
            host="localhost",
            database="study",
            user="postgres",
            password="hyun0421")
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()
        self.cursor.close()

    def insert(self, word, word2):
        insert = 'INSERT INTO "Words" Values ' + "('%s', '%s')" % (word, word2)
        self.cursor.execute(insert)
        self.db.commit()

    def print(self):
        self.cursor.execute('Select * from "Words"')
        rows = self.cursor.fetchall()
        print(rows)


wd = Database()
wd.print()
wd.cursor.fetchall()

