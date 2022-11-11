'''
Mid-term practice exercise

1.  There are two quizzes on geography with questions and answers.
    Let the user choose which one to take.
2.  The user has to choose how many questions they want to answer.
3.  Show the questions to the user, check the answers and count the number of correct answers.
4.  Write the questions that the user got wrong and corresponding correct answers, to a new text file.
5.  Write at least three test cases for the first two functions, no need to test other functions
'''

import random

def create_dict(filename):
    '''
    Loads text file containing questions and answers.
    The question and answers are separated by "?"
    The first row of file is a list of candidate answers,
    you should show that to user.

    :param filename: name of txt file to open and load into a dictionary
    :return: a dictionary with key being questions and values being answers,
    there can be more than one answer, so the value should be a list.
    '''

    f = open(filename)
    quiz_list = f.readlines()
    print('The possible answers for this quiz are:', quiz_list[0])
    quiz_dict = {}
    for i in range(1, len(quiz_list)):
        line = quiz_list[i]
        line_split = line.split('?')
        question = line_split[0].strip()
        questions = question.capitalize() + '?'
        answer = line_split[1].strip()

        lst = quiz_dict.get(questions, [])
        lst.append(answer)
        quiz_dict[questions] = lst

    return quiz_dict


def random_choose(quiz_dict, num):
    '''
    Randomly choose a given number of questions from the dictionary.

    :param quiz_dict: dictionary where questions and answers are stored
    :param num: the number that user entered
    :return: a new question list with the size of 'num'
    '''

    questions = quiz_dict.keys()
    new_questions = random.sample(questions, num)

    return new_questions

def check_answer(question, answer_list):
    '''
    Prompt the user to enter the answer, and check the correctness of the answer.
    If there are more than one answer, all answers should be correct.

    :param question: dictionary key as a string
    :param answer_list: dictionary value as a list of strings
    :return: True or False, depending on the question was answered correctly.
    '''
    global inp

    flag = 0
    print('Answer the following question:')
    print(question)
    inp = input("What's your answer? ")
    inp = inp.split(',')
    print(answer_list)
    answer_list = ''.join(answer_list)
    answer_list = answer_list.split(',')

    for i in range(1,len(answer_list)):
        answer_list[i] = answer_list[i].strip()

    for i in range(1,len(inp)):
        inp[i] = inp[i].strip()

    answer_list.sort()
    inp.sort()

    if (answer_list == inp):
        flag = 1

    print()
    print("---")

    return flag == 1


def count_correct(quiz_dict, question_list):
    '''
    Count how many questions are correctly answered by the user.
    Call check_answer() method here.
    And store the incorrect questions and their original answers to a dictionary.

    :param quiz_dict: dictionary where questions and answers are stored
    :param question_list: a list of questions that user answered
    :return: the number of correct answer and
    '''

    global inp

    num_correct = 0
    incorrect_dict = {}
    answers = []

    for i in range(0,len(question_list)):
            answer = ''.join(quiz_dict.get(question_list[i]))
            answers.append(answer)
            correct = check_answer(question_list[i], answers[-1:])
            if (correct == True):
                num_correct += 1
            else:
                for j in range(0, len(question_list)):
                    lst = incorrect_dict.get(question_list, [])
                    lst.append(inp)
                    incorrect_dict[question_list] = lst

    return num_correct, incorrect_dict


def output_incorrect(incorrect_dict):
    '''
    Allows user to output incorrectly answered questions to a new txt file.

    :param incorrect_dict: keys: incorrectly answered questions, values: original correct answer
    :return: None
    '''

    f = open('Incorrect_Questions.txt', 'w')
    questions = incorrect_dict.keys()
    f.writelines(questions)
    f.close()

    return

def main():
    '''

    Algorithm
    1. User chooses a file between two files.
    2. User chooses number of questions in list to be quizzed on.
    3. Random quiz list is generated.
    4. Quiz the user and count the number of correct answers.
    5. If the user missed any, output the wrong questions and answers to a new file.
    '''
    file_list = ["continents", "oceans"]

    # Print information
    print("Welcome to the vocabulary quiz program.")
    print("Select one of the following quizzes:")

    print(file_list)

    # Print information
    print("Welcome to the vocabulary quiz program.")
    print("Select one of the following quizzes:")

    print(file_list)

    # Ask user to select quiz by typing filename, input should be case insensitive
    filename = input("Please make your selection by typing the file name: ")

    while filename.lower() not in file_list:
        filename = input("Please make a valid selection: ")
    filename += ".txt"

    # Create a dictionary with question being the key and answers being the value.
    flag = 0
    quiz_dict = create_dict(filename)
    number = input('How many questions would you like to answer? ')

    try:
        number = int(number)
    except ValueError as e:
        print('please enter an integer value')

    questions = random_choose(quiz_dict, number)
    num, incorrect = count_correct(quiz_dict, questions)
    print('The number of correct questions is:', num)
    output_incorrect(incorrect)

if __name__ == "__main__":
    main()
