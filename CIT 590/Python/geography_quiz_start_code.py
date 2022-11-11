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

        line = stream.readline()
        line_split = line.split('?')
        question = line_split[0]
        answer = line_split[1]
        answers = answer.split(',')

        for j in range(0,len(answers)):
            quiz_dict[question] += answers[i]

    return quiz_dict


def random_choose(quiz_dict, num):
    '''
    Randomly choose a given number of questions from the dictionary.

    :param quiz_dict: dictionary where questions and answers are stored
    :param num: the number that user entered
    :return: a new question list with the size of 'num'
    '''

    # Generate random numbers
    # You can also use random.sample()


    # Create a new question list


def check_answer(question, answer_list):
    '''
    Prompt the user to enter the answer, and check the correctness of the answer.
    If there are more than one answer, all answers should be correct.

    :param question: dictionary key as a string
    :param answer_list: dictionary value as a list of strings
    :return: True or False, depending on the question was answered correctly.
    '''


    print()
    print("Question:")
    print(question)
    print("What's your answer?")


    print()
    print("---")

    return True


def count_correct(quiz_dict, question_list):
    '''
    Count how many questions are correctly answered by the user.
    Call check_answer() method here.
    And store the incorrect questions and their original answers to a dictionary.

    :param quiz_dict: dictionary where questions and answers are stored
    :param question_list: a list of questions that user answered
    :return: the number of correct answer and
    '''

    num_correct = 0
    incorrect_dict = {}


    return num_correct, incorrect_dict


def output_incorrect(incorrect_dict):
    '''
    Allows user to output incorrectly answered questions to a new txt file.

    :param incorrect_dict: keys: incorrectly answered questions, values: original correct answer
    :return: None
    '''


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
    quiz_dict = create_dict(filename)

    print(create_dict(filename))

    # Ask user to enter how many questions they want to answer


    # make sure we get a valid input


    # Randomly choose a number of questions that user entered


    # Count how many questions are correctly answered by the user.


    # Show correct counts

    # Store the missed question and correct answer into a new file



if __name__ == "__main__":
    main()
