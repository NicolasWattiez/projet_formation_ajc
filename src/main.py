from controller.controller import Controller
from model.config import config
from model.question import Question
from model.qcm import Qcm
from model.jointure import Jointure
from model import connect_db as db

bdd = db.ConnectDb(config)
connexion = bdd.connect()
connexion.autocommit = True
cursor = connexion.cursor()


question = Question(cursor)
qcm = Qcm(cursor)
jointure = Jointure(cursor)

controller = Controller(qcm, question, jointure)

