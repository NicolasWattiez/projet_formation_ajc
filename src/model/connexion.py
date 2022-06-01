from getpass import getpass
from unicodedata import name
import mariadb
from config import config
from question import Question
from qcm import Qcm
from jointure import Jointure
from user import User

 

class Controller():
    def __init__(self, cursor, qcm, question, jointure, user) -> None:
        self.cursor = cursor
        self.qcm = qcm
        self.question = question
        self.jointure = jointure
        self.user = user

    ##### connexion #####

    def query_to_dictionnary(self, cursor):
        desc = cursor.description
        column_names = [col[0] for col in desc]
        dictionnary_list = [dict(zip(column_names, row))  
                for row in cursor.fetchall()]
        return dictionnary_list

    def connexion(self):
        pseudo = input("Enter your pseudo: ")
        # password = input("Enter your password: ")
        password = getpass("Enter your password: ")
        self.user.get_data(pseudo)
        a = self.query_to_dictionnary(self.user.cursor)
        if a == [] :
            statut_user= False
            return "l'utlisateur n'existe pas"
        else :
            b=a[0]["password"] 
            if b == password :
                statut_user= True
                print("l'utilisateur existe")
                return a 
            else :
                statut_user=False
                return "pseudo or password are incorrect"




        







#####
if __name__ == "__main__":
    import config 
    import connect_db as db

    bdd = db.ConnectDb(config.config)
    connexion = bdd.connect()
    connexion.autocommit = True
    cursor = connexion.cursor()

    question = Question(cursor)
    qcm = Qcm(cursor)
    jointure = Jointure(cursor)
    user=User(cursor)
    test_controller = Controller(cursor,question,qcm,jointure,user)

    # test_qcm.update_data()
    a=input('id de la question:')
   
    
    print(test_controller.connexion())