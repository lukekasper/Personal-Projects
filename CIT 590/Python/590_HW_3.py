import random
def print_instructions():
    '''Prints the games instructions.'''
    print('',
          '~~~~~~ Ready to play PIG?! ~~~~~~','',
          'Rules of the game:',
          '- Player 1 rolls the die',
          '- After each roll, he/she can decide whether to stop or continue rolling',
          '- If the player stops rolling, all the previous rolls are added to the total score',
          '- If a 6 is rolled at any time, the score for that turn is 0',
          '- Player 2 then repeats this process',
          '- The players alternate turns until one player reaches a score of 50',
          '- If player 1 reaches 50 first, player 2 gets one additional roll',
          '- If there is a tie, both players will get one additional turn to break the tie', '', sep = '\n')
    return

def roll():
    '''Simulates a roll by generating a random integer between 1 and 6.'''

    #generates a random integer 1-6 to simulate a dice roll
    roll = random.randint(1, 6)
    return roll

def computer_move(computer_score, human_score):
    '''Simulates the computers turn.
       If the computer is winning it will roll between 1 and 4 times.
       If the human (Player 2) is winning, it will gamble more aggressively and roll between 3 and 6 times.
       The computer will never roll more than 6 times as this will statistically lead to a loss.'''

    #initialize variables
    n = 1
    roll_count = 0
    nroll = 0
    score1 = 0

    if (human_score <= computer_score):

        #generates a random int 1-4 to simulate the number of rolls in a turn for the computer
        rolln = random.randint(1,4)

        while (n <= rolln):
            nroll = roll()
            print('Player 1 rolled a:', nroll)

            #if a 6 is rolled the score is 0 and the turn is over
            if (nroll == 6):                    
                score1 = 0
                print('A six was rolled!')
                print('')
                return score1
            
            #any other roll adds it to the score for that turn and increases the roll count
            else:                               
                score1 = score1 + nroll
                roll_count += 1
                n += 1

    #if the computer is losing it gambles more aggressively and rolls between 3 and 6 times
    elif (human_score > computer_score):
        rolln = random.randint(3,6)

        while (n <= rolln):
            nroll = roll()
            print('Player 1 rolled a:', nroll)

            if (nroll == 6):
                score1 = 0
                print('A six was rolled!')
                print('Score for this turn is 0', '\n')
                return score1
            else:
                score1 = score1 + nroll
                roll_count += 1
                n += 1
    print('Score for this turn is:', score1, '\n' + 'Number of rolls for this turn:', roll_count)
    print('')

    return score1

def human_move(computer_score, human_score):
    '''Simulates a turn for the user.
       Adds up each roll for the user until he/she decides to stop or rolls a 6.'''

    #initialize variables
    score2 = 0
    ans = True
    prompt = 'yes'

    #first roll is automatic
    roll1 = roll()

    #if you roll a 6 your score is 0 and the turn is over
    if (roll1 == 6):
        score2 = 0
        print('Sorry but you rolled a 6! :(')
        return score2
    
    #any other roll sets your score as that roll and calls the prompt function
    else:
        score2 = roll1
        print('You rolled a:', roll1)
        ans = ask_yes_or_no(prompt)

        #continues to call the prompt function and sum the rolls as long as your answer is "True" or roll is not a 6
        #(see ask_yes_or_no(prompt))
        if (ans == True):
            while (ans == True):
                nroll = roll()

                if (nroll == 6):
                    score2 = 0
                    print('Sorry but you rolled a 6! :(')
                    break
                else:
                    score2 = score2 + nroll
                    print('You rolled a:', nroll)
                    ans = ask_yes_or_no(prompt)

        print('')
        print('Your score for this turn is:', score2)
        print('')
        
        return score2
                
def ask_yes_or_no(prompt):
    '''Continuosly prompts the user to roll again.
       Entering a 'y' or 'Y' reruns the function.
       Entering a 'n' or 'N' breaks the loop and returns the total score.
       Any other string will result in a reprompt for a valid input.'''

    #initialize variables
    b = 1

    #continuously prompt user for if he/she would like to roll again
    while (b == 1):
        prompt = input('Would you like to roll again? ')

        #No entry reprompts the user
        if (prompt == ''):                                                      
            print('Please enter a valid response','help(ask_yes_or_no) for more information', sep = '\n')
            print('')
            continue

        #Entering a 'n' or 'N' exits the loop and sets answer = False
        elif (prompt[0] == 'n' or prompt[0] == 'N'):                            
            ans = False
            b = 2

        #Entering a 'y' or 'Y' exits the loop and sets answer = True
        elif (prompt[0] == 'y' or prompt[0] == 'Y'):                           
            ans = True
            b = 2

        #Entering any other string reprompts the user
        else:                                                                   
            print('Please enter a valid response','help(ask_yes_or_no) for more information', sep = '\n')
            print('')
            continue

    return ans

def is_game_over(computer_score, human_score):
    '''Sets the criteria for the game being over when a player reaches a score of 50.'''

    #set global variables
    global p1_score
    global p2_score

    #sets criteria for the end of the game
    if (p1_score >= 50 or p2_score >= 50):
        game_over = True
    else:
        game_over = False

    return game_over

def show_current_status(computer_score, human_score):
    '''Displays the current status of the game after each turn.'''

    #set global variables
    global p1_score
    global p2_score

    #calculates and displays the difference of the scores and who is winning
    difference = abs(p1_score - p2_score)
    print('Player 1 score:', p1_score, '\n' + 'Player 2 score:', p2_score)

    if (p1_score > p2_score):
        print('Player 2 is losing by:', difference)
        
    elif (p1_score < p2_score):
        print('Player 2 is winning by:', difference)
        
    else:
        print('The game is tied!')

    print('')

    return

def show_final_results(computer_score, human_score):
    '''Displays the final score and who won the game.'''
    
    #set global variables
    global p1_score
    global p2_score

    #calculates and displays the winner of the game and by how much
    difference = abs(p1_score - p2_score)

    if (p1_score > p2_score):
        print('Player 2 LOSES by:', difference)
        
    elif (p1_score < p2_score):
        print('Player 2 WINS by:', difference)

    return

def turn(computer_score, human_score):
    '''Simulates a complete turn for both players.'''

    #set global variables
    global p1_score
    global p2_score
    
    #runs a complete turn for each player and displays current status (helper function)
    score1 = computer_move(p1_score, p2_score)
    p1_score = score1 + p1_score
    show_current_status(p1_score, p2_score)

    score2 = human_move(p1_score, p2_score)
    p2_score = score2 + p2_score
    show_current_status(p1_score, p2_score)

    return p1_score, p2_score

def replay_game(c):
    '''Prompts the user if he/she would like to replay the game.
       Same syntax as "ask_yes_or_no" function help(ask_yes_or_no) for details.'''

    #set while loop flag
    b = 1

    #continues to prompt the user if he/she would like to play again (helper function)
    #same methodology as ask_yes_or_no (see for details)
    while (c == 1):
        inp = input('Would you like to play again? ')
        if (inp == ''):
            print('Sorry, please enter a valid response ', 'help(ask_yes_or_no) for more information','',sep = '\n')
            continue
        elif (inp[0] == 'n' or inp[0] == 'N'):
            b = 2
            c = 2
        elif (inp[0] == 'y' or inp[0] == 'Y'):
            c = 2
        else:
            print('Sorry, please enter a valid response ', 'help(ask_yes_or_no) for more information','',sep = '\n')
            continue
            
    return b
        
def main():
    '''Main functions that runs all subsequent functions and simulates the overall game.'''

    #set global variables
    global p1_score
    global p2_score
    
    print_instructions()
    b = 1

    #while loop to rerun the game if the user desides (set by play_again function)
    while (b == 1):

        print('')

        #initialize variables and flags
        p1_score = 0
        p2_score = 0
        flag = 1
        a = False
        
        #while loop to rerun earch player's turn until the game is considered over (set by is_game_over function) 
        while (a == False):
        
            [p1_score, p2_score] = turn(p1_score, p2_score)
    
            if (p2_score == p1_score and p2_score >= 50):

                while (p1_score == p2_score):
                    [p1_score,p2_score] = turn(p1_score, p2_score)
    
            a = is_game_over(p1_score, p2_score)

        show_final_results(p1_score, p2_score)
        
        b = replay_game(flag)
        
    return

#runs the main function
if (__name__ == '__main__'):
    main()   
        
