
from unicodedata import name
import table
import mariadb


class Question():
    def __init__(self, cursor):
        table.Table(cursor)
        self.__name = ''
    
    def get_name(self):
        return self.__name

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name


    def get_data(self):
<<<<<<< HEAD
        # self.cursor.execute("")
        pass
=======
        cursor=connexion.cursor()
        cursor.execute('SELECT * FROM questions WHERE id = "1";')
        print_data=cursor.fetchone()
        return print_data

>>>>>>> 55a3ad3290a45371e5fc330e7d2deef69bafb8ca

    def insert_data(self):
        try:
            cursor=connexion.cursor()
            cursor.execute('INSERT INTO questions (name,answers,correct_answer) VALUES ("test ?","a,b,c","c");')
            connexion.commit()
            return 'La question a bien été ajoutée'
        except mariadb.Error as e:
            return 'Erreur lors de l\'ajout de la question {e} '


    def remove_data(self):
        try:
            cursor = connexion.cursor()
            cursor.execute('DELETE FROM questions WHERE id = "5";')
            connexion.commit()
            return 'La question à bien été supprimée'
        except mariadb.Error as e:
            return 'Erreur lors de la suppression de la question {e}' 

    def update_data(self):
        try:
            cursor = connexion.cursor()
            cursor.execute('UPDATE questions SET `correct_answer` = "a" WHERE `id` = 6;')
            connexion.commit()
            return 'La réponse a bien été modifiée'
        except mariadb.Error as e:
            return ' Erreur lors de la modification de la réponse {e}' 





#####

import config
import connect_db as db

bdd = db.ConnectDb(config.config)
connexion = bdd.connect()
cursor = connexion.cursor()
<<<<<<< HEAD

cursor.execute('INSERT INTO `qcm` VALUES (1, "Histoire");')
cursor.execute('SELECT * FROM qcm')
print(cursor.fetchall())
# déclarer le cursor ici

=======
>>>>>>> 55a3ad3290a45371e5fc330e7d2deef69bafb8ca
test_question = Question(cursor)

# test_qcm.update_data()
print(test_question.update_data())


