from controller.controller import Controller
from model import *
from controller import *
from model.config import config
from model.question import Question
from model.qcm import Qcm
from model.jointure import Jointure
from model.user import User
# from model.jointure import Us

from model import connect_db as db

bdd = db.ConnectDb(config)
connexion = bdd.connect()
connexion.autocommit = True
cursor = connexion.cursor()


question = Question(cursor)
qcm = Qcm(cursor)
jointure = Jointure(cursor)
user= User(cursor)
# users = Users(cursor)

test = Controller(qcm, question, jointure,user)
a=input('id :')
b= {"name": "fruit ?", "answers": "orange,bananane,kiwi", "correct_answer": "kiwi"}
print(test.update_question())

# print(test.get_qcm())
# print(test.get_question())

# test.connexion()

# questions = test.select_qcm()
# test.practice_qcm(questions)

# test.create_qcm()
# print(test.get_qcm())


# test.remove_qcm()
# print(test.get_qcm())