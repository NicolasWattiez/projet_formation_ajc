from controller.controller import Controller
from model import *
from controller import *
from model.config import config
from model.question import Question
from model.qcm import Qcm


from model import connect_db as db

bdd = db.ConnectDb(config)
connexion = bdd.connect()
cursor = connexion.cursor()


question = Question(cursor)
qcm = Qcm(cursor)

test = Controller(qcm, question)

print(test.get_qcm())
connexion.commit()