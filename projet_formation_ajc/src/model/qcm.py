from unicodedata import name
import table
import mariadb


class Qcm:
    
    def __init__(self, cursor):
        table.Table(cursor)
        self.__name = ''
    
    def get_name(self):
        return self.__name

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name

    def get_data(self):
        cursor=connexion.cursor()
        cursor.execute('SELECT * FROM qcm WHERE name = "Musique";')
        print_data=cursor.fetchone()
        return print_data

    def insert_data(self):
        try:
            cursor=connexion.cursor()
            cursor.execute('INSERT INTO qcm (`name`) VALUES ("ciné");')
            connexion.commit()
            return 'Le QCM a bien été ajoutée'
        except mariadb.Error as e:
            return 'Erreur lors de l\'ajout du nouveau qcm {e} '


    def remove_data(self):
        try:
            cursor = connexion.cursor()
            cursor.execute('DELETE FROM qcm WHERE name = "ciné";')
            connexion.commit()
            return 'La machine à bien été supprimée'
        except mariadb.Error as e:
            return 'Erreur lors de la suppression du qcm {e}' 



    def update_data(self):
        try:
            cursor = connexion.cursor()
            cursor.execute('UPDATE qcm SET `name` = "film" WHERE `id` = 4;')
            connexion.commit()
            return 'La machine a bien été modifiée'
        except mariadb.Error as e:
            return ' Erreur lors de la modification du qcm {e}' 

####
import config
import connect_db as db

bdd = db.ConnectDb(config.config)
connexion = bdd.connect()
cursor = connexion.cursor()
test_qcm = Qcm(cursor)

test_qcm.get_data()