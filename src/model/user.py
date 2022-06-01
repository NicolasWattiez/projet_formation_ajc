# Créer une classe user :
# fonction :
#    - crétion d'un user
#    - recuperer user en foction du nom ()
# 
from unicodedata import name
import mariadb

class User:
    def __init__(self, cursor):
        self.cursor = cursor
        self.__name = ''

    def get_data(self,name):
        name_user=name
        # cursor=connexion.cursor()
        self.cursor.execute('SELECT * FROM users WHERE pseudo = ?;',
        (name_user,)
        )


    def create_user(self,name,password):
        user_name=name
        user_password=password
        self.cursor.execute('INSERT INTO `users`(pseudo,password,created_at) VALUES (? ,?, NOW());',
        (user_name,user_password)
        )




#### 
if __name__ == "__main__":
    import config
    import connect_db as db

    bdd = db.ConnectDb(config.config)
    connexion = bdd.connect()
    connexion.autocommit = True
    cursor = connexion.cursor()
    test_user = User(cursor)

   # test_qcm.update_data()
    a=input('pseudo utilisateur :')
    b=input('paswword :')
    print(test_user.get_data(a))
    print(cursor.fetchall())