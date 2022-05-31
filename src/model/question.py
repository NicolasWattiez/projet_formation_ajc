from table import Table


class Question(Table):
    def __init__(self, cursor):
        Table.__init__(self, cursor)


    def get_data(self):
        # self.cursor.execute("")
        pass

    def insert_data(self):
        pass

    def remove_data(self):
        pass

    def update_data(self):
        pass





#####

import mariadb
import config
import connect_db as db

bdd = db.ConnectDb(config.config)
connexion = bdd.connect()
cursor = connexion.cursor()

cursor.execute('INSERT INTO `qcm` VALUES (1, "Histoire");')
cursor.execute('SELECT * FROM qcm')
print(cursor.fetchall())
# déclarer le cursor ici

test_question = Question(cursor)


test_question.get_data()

