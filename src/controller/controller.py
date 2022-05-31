
class Controller():
    def __init__(self, qcm, question) -> None:
        self.qcm = qcm
        self.question = question

    ##### connexion #####

    def connexion():
        pseudo = input("Enter your pseudo: ")
        password = input("Enter your password")
        pass




    #### Admin ####

    def create_qcm():
        # ask for qcm name
        # insert new qcm
        # ask if the user want to add questions to this qcm
            # get id qcm
            # call create_question() => return question values
            # question_id from question values
            # call add_question_to_qcm(id_qcm, id_question)
        pass


    def remove_qcm():
        # get id_qcm
        # question do you want to also remove related question # WARNING the questions will also be removed from all qcm
            # get related id_question
        # remove in join_qcm_questions by qcm_id 
            # and remove related id_question
        # remove qcm_id in qcm
            # remove id_question from question
        # commit change
        pass

    def update_qcm():
        # check if qcm exists
        pass

    def create_question():
        question_values = {"name": "", "answers": "", "correct_answer": ""}
        question_values["name"]
        # ask what is the question
        # ask what are the answers
        # ask what is the correct answers
        # insert new question
        return question_values
        # ask if the user want to add the question to a qcm (put that outside?)

    def remove_question():
        # remove question by id
        # remove id_question from join table
        pass

    def update_question():
        # check if question exists
        pass

    def add_question_to_qcm(id_question, id_qcm):
        pass

    def remove_question_from_qcm(id_question, id_qcm):
        pass


    ##### User ####

    def select_qcm(qcms):
        for qcm in qcms:
            print(qcm["name"])
        user_choice = input(
            "Please, enter the name of your choice"
        )
        # loop back if incorrect answer
        return user_choice



    def practice_qcm(questions):
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

    def query_to_dictionnary(cursor):
        desc = cursor.description
        column_names = [col[0] for col in desc]
        dictionnary_list = [dict(zip(column_names, row))  
                for row in cursor.fetchall()]
        return dictionnary_list




