
from unicodedata import name
# import table
import mariadb


class Question():
    def __init__(self, cursor):
        self.cursor = cursor
        self.__name = ''
    
    def get_name(self):
        return self.__name

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name


    def get_data(self,id):
        numero_id=id
        # cursor=connexion.cursor()
        self.cursor.execute('SELECT * FROM questions WHERE id = ?;',
        (numero_id,)
        )
        print_data=cursor.fetchone()
        return print_data


    def insert_data(self,question_values):
        question=question_values["name"]
        all_answers=question_values["answers"]
        good_answer=question_values["correct_answer"]
        try:
            cursor = connexion.cursor()
            cursor.execute('INSERT INTO questions (name,answers,correct_answer) VALUES (?,?,?);',
            (question,all_answers,good_answer)
            )
            connexion.commit()
            return 'La question a bien été ajoutée'
        except mariadb.Error as e:
            return 'Erreur lors de l\'ajout de la question {e} '


    def remove_data(self,id):
        numero_id=id
        try:
            cursor = connexion.cursor()
            cursor.execute('DELETE FROM questions WHERE id = ?;',
            (numero_id,)
            )
            connexion.commit()
            return 'La question à bien été supprimée'
        except mariadb.Error as e:
            return 'Erreur lors de la suppression de la question {e}' 

    def update_data(self,id,new_question_values):
        numero_id=id 
        new_question=new_question_values["name"] 
        new_all_answers=new_question_values["answers"] 
        new_good_answer=new_question_values["correct_answer"] 
        try:
            cursor = connexion.cursor()
            cursor.execute('UPDATE questions SET `name` = ? , answers = ?, correct_answer = ? WHERE `id` = ?;',
            (new_question,new_all_answers,new_good_answer,numero_id)
            )
            connexion.commit()
            return 'La réponse a bien été modifiée'
        except mariadb.Error as e:
            return ' Erreur lors de la modification de la réponse {e}' 





#####
if __name__ == "__main__":
    import config
    import connect_db as db

    bdd = db.ConnectDb(config.config)
    connexion = bdd.connect()
    cursor = connexion.cursor()
    test_question = Question(cursor)

    # test_qcm.update_data()
    a=input('id de la question:')
    question_values = {"name": "Ta couleur favorite ?", "answers": "rouge,vert,noir", "correct_answer": "vert"}
    new_question_values ={"name": "Ta couleur favorite ?", "answers": "rouge,vert,noir", "correct_answer": "noir"}
    print(test_question.get_data(a))


