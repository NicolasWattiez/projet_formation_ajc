# créer une classe (jointure)
# methode :
#   - fonction insert id qcm id question avec 
#   - fonction supprimer une ligne en fonction id qcm et id question
#   - fonction supprimer une ligne en fonction id qcm
#   - fonction supprimer une ligne en fonction id question
#   - recuperer tout les id question pour un qcm  

from unicodedata import name
import mariadb

class Jointure:
    def __init__(self, cursor):
        self.cursor = cursor
        self.__name = ''


    def link_qcm_question(self,id_qcm,id_question):
        idqcm=id_qcm
        idquestion=id_question
        try:
            # cursor = connexion.cursor()
            self.cursor.execute('INSERT INTO join_qcm_questions (question_id,qcm_id) VALUES (?,?);',
            (idquestion,idqcm)
            )
            # connexion.commit()
            return 'le lien entre la réponse et le qcm a été fait'
        except mariadb.Error as e:
            return ' Erreur lors de la création du lien{e}'  


    def delete_link_qcm_question(self,id_qcm,id_question):
        idqcm=id_qcm
        idquestion=id_question
        try:
            # cursor = connexion.cursor()
            self.cursor.execute('DELETE FROM join_qcm_questions WHERE question_id = ? AND qcm_id = ? ;',
            (idquestion,idqcm)
            )
            # connexion.commit()
            return 'le lien entre la réponse et le qcm a été supprimé'
        except mariadb.Error as e:
            return ' Erreur lors de la création du lien{e}'  
    
    def delete_all_link_qcm(self,id_qcm):
        idqcm=id_qcm
        try:
            # cursor = connexion.cursor()
            self.cursor.execute('DELETE FROM join_qcm_questions WHERE qcm_id = ? ;',
            (idqcm,)
            )
            # connexion.commit()
            return 'tout les liens liés a ce qcm ont été supprimé'
        except mariadb.Error as e:
            return ' Erreur lors de la création du lien{e}'  

    def delete_all_link_question(self,id_question):
        idquestion=id_question
        try:
            # cursor = connexion.cursor()
            self.cursor.execute('DELETE FROM join_qcm_questions WHERE question_id = ? ;',
            (idquestion,)
            )
            # connexion.commit()
            return 'tout les liens liés a cette question ont été supprimé'
        except mariadb.Error as e:
            return ' Erreur lors de la création du lien{e}' 

    def find_questions_from_qcm(self,id_qcm):
        idqcm=id_qcm
        try:
            # cursor = connexion.cursor()
            self.cursor.execute('SELECT id,name,answers,correct_answer FROM (SElECT * FROM questions INNER JOIN join_qcm_questions WHERE join_qcm_questions.question_id=questions.id ) AS a WHERE qcm_id = ?;',
            (idqcm,)
            )
            # list_id_question=cursor.fetchall()k
            # connexion.commit()
            # return list_id_question
        except mariadb.Error as e:
            return ' Erreur lors de la création du lien{e}'  



#### 
if __name__ == "__main__":
    import config
    import connect_db as db

    bdd = db.ConnectDb(config.config)
    connexion = bdd.connect()
    connexion.autocommit = True
    cursor = connexion.cursor()
    test_jointure = Jointure(cursor)

    # test_qcm.update_data()
    a=input('id qcm :')
    b=input('id question:')
    print(test_jointure.find_questions_from_qcm(a))
    print(cursor.fetchall())      

