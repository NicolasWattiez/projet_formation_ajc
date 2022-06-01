from getpass import getpass

class Controller():
    def __init__(self, qcm, question, jointure, users) -> None:
        self.qcm = qcm
        self.question = question
        self.jointure = jointure
        self.users = users

    ##### connexion #####

    def connexion(self):
        pseudo = input("Enter your pseudo: ")
        # password = input("Enter your password: ")
        password = getpass("Enter your password: ")
        




    #### Admin ####

    def get_qcm(self):
        self.qcm.get_data()
        return self.query_to_dictionnary(self.qcm.cursor)

    def create_qcm(self):
        new_qcm_name = input('Enter the name of the new qcm: ')
        self.qcm.insert_data(new_qcm_name)
        user_choice = input('Enter "yes" if you want to add question now: ')
        if user_choice == 'yes':
            self.qcm.get_data(new_qcm_name)
            dict_new_qcm = self.query_to_dictionnary(self.qcm.cursor)
            adding_questions = True
            while adding_questions:
                new_question_values = self.create_question()
                dict_new_question = self.question.get_data_by_name(new_question_values["name"])
                self.add_question_to_qcm(dict_new_qcm["id"], dict_new_question["id"])



    def remove_qcm(self):
        name_qcm_to_delete = input("Enter the name of the qcm to delete: ")
        id_qcm_to_delete = self.qcm.get_data(name_qcm_to_delete)
        user_choice = input(
            """Enter "yes" if you want to remove all related questions now 
            (WARNING, do note that all questions linked to this qcm will be removed and this cannot be undone): """
            )
        if user_choice == "yes":
            self.jointure.find_questions_from_qcm(id_qcm_to_delete)
            dict_related_questions = self.query_to_dictionnary(self.qcm.cursor)
            self.jointure.delete_all_link_qcm(id_qcm_to_delete)
            for question in dict_related_questions:
                self.question.remove_data(question["id"])
        self.qcm.remove_data(name_qcm_to_delete)

    def update_qcm(self):
        name_qcm_to_update = input("Enter the name of the qcm to delete: ")
        if self.qcm.get_data(name_qcm_to_update) != []: 
            self.question.update_data()
        else:
            print("The qcm doesn't exist!")


    def get_question(self):
        self.question.get_data()
        return self.query_to_dictionnary(self.question.cursor)


    def create_question(self):
        question_values = {"name": "", "answers": "", "correct_answer": ""}
        question_values["name"]
        question = input("Enter the question: ")
        answers = input("Enter the answers: ")
        correct_answer = input("Enter the question: ")
        question_values.update({"name": question, "answers": answers, "correct_answer": correct_answer})
        self.question.insert_data(question_values)
        return question_values

    def remove_question(self, id):
        self.jointure.delete_all_link_question(id)
        self.question.remove_data(id)

    def update_question(self):
        id_question_to_update = input("Enter the name of the qcm to delete: ")
        if self.question.get_data(id_question_to_update) != []: 
            self.question.update_data()
        else:
            print("The question doesn't exist!")


    def add_question_to_qcm(self, id_qcm, id_question):
        self.jointure.link_qcm_question(id_qcm, id_question)

    def remove_question_from_qcm(self, id_qcm,  id_question):
        self.jointure.delete_link_qcm_question(id_qcm, id_question)


    ##### User ####

    def select_qcm(self, qcms):
        print("List qcm")
        for qcm in qcms:
            print("- ", qcm["name"])
        user_choice = input(
            "Please, enter the name of the qcm you want to try: "
        )
        # loop back if incorrect answer
        dict_qcm = self.qcm.get_data(user_choice)
        self.jointure.find_questions_from_qcm(dict_qcm)
        questions = self.query_to_dictionnary(self.jointure.cursor)
        print(questions)
        return questions



    def practice_qcm(self, questions):
        for question in questions:
            print(question["name"])
            for answer in question["answers"].split(","):
                print(answer)
            user_answer = input("Write the corrert answer: ")
            # loop back if answers is not in answers
            if user_answer == question["correct_answer"]:
                print("You are correct!")
            else:
                print("Sorry but the correct answer was ", 
                question["correct_answer"])
            print("\n")
            



    # move to table
    # Taken from https://stackoverflow.com/questions/28755505/how-to-convert-sql-query-results-into-a-python-dictionary

    def query_to_dictionnary(self, cursor):
        desc = cursor.description
        column_names = [col[0] for col in desc]
        dictionnary_list = [dict(zip(column_names, row))  
                for row in cursor.fetchall()]
        return dictionnary_list




