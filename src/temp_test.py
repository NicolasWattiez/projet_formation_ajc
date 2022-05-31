############# test ##################


import mariadb
from model import config
from model import connect_db as db

bdd = db.ConnectDb(config.config)
connexion = bdd.connect()


from controller import controller

