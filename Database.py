"""
This is the database
"""
import psycopg2


class Database:
    def __init__(self):
        try:
            self.db = psycopg2.connect(
                host="localhost",
                database="study",
                user="postgres",
                password="hyun0421")
        except Exception as e:
            print("DB err ", e)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()
        self.cursor.close()

    def newset(self, word):
        try:
            insert = 'INSERT INTO "sets" Values ' + "('%s')" % word
            self.cursor.execute(insert)
            self.db.commit()
        except Exception as e:
            print("DB err ", e)

    def insertword(self, sets, word, word2):
        try:
            insert = 'INSERT INTO "words" Values ' + "('%s', '%s', '%s')" % (sets, word, word2)
            self.cursor.execute(insert)
            self.db.commit()
        except Exception as e:
            print("DB err ", e)

    def getset(self):
        try:
            self.cursor.execute('Select "setName" from "sets"')
            rows = self.cursor.fetchall()
            self.db.commit()
            return rows
        except Exception as e:
            print("DB err ", e)

    def getworddef(self, sets):
        try:
            sen = "'%s'" % sets
            self.cursor.execute('Select "w", "d" from "words" where "setName" = ' + sen)
            rows = self.cursor.fetchall()
            self.db.commit()
            return rows
        except Exception as e:
            print("DB err ", e)
            return ""

    def getstaredworddef(self, sets):
        try:
            sen = "'%s'" % sets
            self.cursor.execute('Select "w", "d" from "words" where "s" is true and "setName" = ' + sen)
            rows = self.cursor.fetchall()
            self.db.commit()
            return rows
        except Exception as e:
            print("DB err ", e)
            return ""

    def startheword(self, word):
        try:
            sen = "'%s'" % word
            self.cursor.execute('UPDATE "words" SET "s" = True WHERE "w" = ' + sen)
        except Exception as e:
            print("DB err ", e)

    def destartheword(self, word):
        try:
            sen = "'%s'" % word
            self.cursor.execute('UPDATE "words" SET "s" = False WHERE "w" = ' + sen)
        except Exception as e:
            print("DB err ", e)