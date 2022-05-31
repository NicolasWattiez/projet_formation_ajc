
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


    def get_data(self,id):
        numero_id=id
        cursor=connexion.cursor()
        cursor.execute('SELECT * FROM questions WHERE id = ?;',
        (numero_id,)
        )
        print_data=cursor.fetchone()
        return print_data


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
test_question = Question(cursor)

# test_qcm.update_data()
a=input('id de la question:')
print(test_question.get_data(a))


