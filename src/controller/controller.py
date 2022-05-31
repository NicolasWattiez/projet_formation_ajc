



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
        




# Taken from https://stackoverflow.com/questions/28755505/how-to-convert-sql-query-results-into-a-python-dictionary

def query_to_dictionnary(cursor):
    desc = cursor.description
    column_names = [col[0] for col in desc]
    dictionnary_list = [dict(zip(column_names, row))  
            for row in cursor.fetchall()]
    return dictionnary_list




