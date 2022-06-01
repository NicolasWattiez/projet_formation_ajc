from unicodedata import name
import mariadb


class Qcm:
    
    def __init__(self, cursor):
        self.cursor = cursor
        self.__name = ''
    
    def get_name(self):
        return self.__name

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name

    def get_data(self,name=None):
        name_qcm=name
        print("name")
        print("name == None?", name == None)
        # cursor=connexion.cursor()
        if name == None:
            print("all")
            self.cursor.execute('SELECT * FROM qcm;')      
        else:
            print("one")
            self.cursor.execute('SELECT * FROM qcm WHERE name = ?;',
            (name_qcm,)
            )

    def insert_data(self,name):
        new_qcm=name
        try:
            # cursor=connexion.cursor()
            self.cursor.execute('INSERT INTO qcm (`name`) VALUES (?);',
            (new_qcm,)
            )
            # connexion.commit()
            return 'Le QCM a bien été ajoutée'
        except mariadb.Error as e:
            return 'Erreur lors de l\'ajout du nouveau qcm {e} '


    def remove_data(self,name):
        delete_qcm=name
        try:
            # cursor = connexion.cursor()
            self.cursor.execute('DELETE FROM qcm WHERE name = ?;',
            (delete_qcm,)
            )
            # connexion.commit()
            return 'Le QCM à bien été supprimée'
        except mariadb.Error as e:
            return 'Erreur lors de la suppression du qcm {e}' 



    def update_data(self,name,new_name):
        update_qcm=name
        new_qcm_name=new_name
        try:
            # cursor = connexion.cursor()
            self.cursor.execute('UPDATE qcm SET `name` = ? WHERE `name` = ?;',
            (new_qcm_name,update_qcm)
            )
            # connexion.commit()
            return 'Le QCM a bien été modifiée'
        except mariadb.Error as e:
            return ' Erreur lors de la modification du qcm {e}' 

if __name__ == "__main__":
    import config
    import connect_db as db

    bdd = db.ConnectDb(config.config)
    connexion = bdd.connect()
    connexion.autocommit = True
    cursor = connexion.cursor()
    test_qcm = Qcm(cursor)

    # test_qcm.update_data()
    # a=input('nom du qcm :')
    # b=input('nouveau nom du qcm :')
    print(test_qcm.get_data("Musique"))
    


   

