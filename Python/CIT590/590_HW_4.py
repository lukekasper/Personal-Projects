import random

def print_instructions():
    '''Prints the games instructions.'''
    print('',
          '~~~~~~Ready to Play Tower Blaster?!~~~~~~','',
          'Rules of the game:',
          '- each player recieves 10 cards in their tower',
          '- at the start of each turn, a player can choose to:',
          '     - draw from the discard pile (face up)',
          '     - or draw an unknown card from the main pile',
          '- the player can then replace one of the cards in their tower with the drawn card',
          '- the replaced card then goes into the discard pile',
          '- if the player draws from the main pile, he/she may place that card in the discard pile',
          '- the game is over when one of the players achieves a tower in descending order (stable)','', sep = '\n')
          
          

def setup_bricks():
    '''Creates a main pile of 60 bricks and a discard pile of 0 bricks.'''

    #set global variables
    global main_pile
    global discard

    #initializes variables
    main_pile = []
    discard = []

    #creates a list of integers from 1-60
    for i in range(1,61):
            main_pile.append(i)
            
    return (main_pile, discard)

def shuffle_bricks(bricks):
    '''Shuffles the main pile of bricks.'''

    #randomely orient integers in pile
    random.shuffle(bricks)
    
    return

def check_bricks(main_pile, discard):
    '''Checks to see if any bricks are left in the main pile.
       If the main pile is empty, it shuffles the discard pile
       and resets that as the main pile.'''

    #if the main deck is empty, shuffle discard pile
    if (main_pile == []):
        random.shuffle(discard)

        #sets shuffled pile to main pile and the first card as the new discard pile
        main_pile = discard
        discard = main_pile[0]

    return (main_pile, discard)

def check_tower_blaster(tower):
    '''Checks to see if the tower is in ascending order.
       Returns a boolean result.'''

    #creates a new tower list and sorts it
    flag = 0
    tower1 = tower[:]
    tower1.sort()

    #if the sorted list matches the original tower, return True
    if (tower1 == tower): 
        flag = 1

    return flag == 1

def get_top_brick(brick_pile):
    '''Gets the top brick from one of the piles (main, discard, or one of the towers).
       Removes that brick from the current pile it was in.'''
    
    #set global variables
    global main_pile
    global discard
    global my_tower
    global comp_tower

    #determins which pile the brick is coming from
    if (brick_pile == main_pile):
        main_copy = main_pile.copy()
        
        #returns the first card of that pile
        main1 = main_copy[0]

        #deletes that crad from the that pile
        main_pile.pop(0)
        return main1
    
    elif (brick_pile == discard):
        discard_copy = discard.copy()
        discard1 = discard_copy[0]
        discard.pop(0)
        return discard1
    
    elif (brick_pile == my_tower):
        my_tower_copy = my_tower.copy()
        my_tower1 = my_tower_copy[0]
        my_tower.pop(0)
        return my_tower1
    
    else:
        comp_tower_copy = comp_tower.copy()
        comp_tower1 = comp_tower_copy[0]
        comp_tower.pop(0)
        return comp_tower1

def deal_initial_bricks(main_pile):
    '''Starts the game by dealing two sets of 10 bricks from the main pile.'''

    #set global variables
    global my_tower
    global comp_tower

    #initialize variables
    my_tower = []
    comp_tower = []

    #deals every other card to first the computers tower, and then the users
    for i in range(0,10):
        comp_tower.append(main_pile[2*i])
        my_tower.append(main_pile[2*i+1])

    #deletes those cards from the main pile
    del main_pile[0:21]
        
    #reverses the two towers to fit the convention of the game
    comp_tower.reverse()
    my_tower.reverse()
    
    return (my_tower,comp_tower)

def add_brick_to_discard(brick, discard):
    '''Adds the specified brick to the discard pile.'''

    #add brick to the discard pile
    discard.insert(0,brick)

    return

def find_and_replace(new_brick, brick_to_be_replaced, tower, discard):
    '''Replaces a brick from the tower with the a new brick.
       Also places the old brick in the discard pile.
       If the specified brick is in the pile return True
       Else, return false.'''

    #loops through the list of tower values
    for i in range(0,len(tower)):

        #checks to see if the brick specified is in the tower
        if (brick_to_be_replaced == tower[i]):

            #if it is, replace it with the new brick
            tower[i] = new_brick

            #place the old brick in the discard pile
            add_brick_to_discard(brick_to_be_replaced,discard)
            return True
            
    return False

def computer_play(tower, main_pile, discard):
    '''Simulates the computers turn.
       The computer will try to place the discard brick in evenly spaced ranges in its tower.
       For example: if discard is 1-6 and there is not a 1-6 on the top of the tower, replace index 0 in tower with discard.
       If discard is 7-12 and there is not a 7-12 in the tower in 1st index of the tower, replace that card with discard...ect.
       Oherwise, draw from main pile and follow similar scheme.
       If a card in that range is already in the tower in the correct slot, put the picked card directly in the discard pile.'''

    #initialize flags
    flag = 0
    flag1 = 0

    #if the discard card is between 0-4 place directly at the top
    if (discard[0] <= 4):
        print('Computer has drawn a:', discard[0], 'from the discard pile')
        print(discard[0], 'has replaced', tower[0], 'in the computer tower')
        print('')
        find_and_replace(discard[0], tower[0], tower, discard)

    #if the discard card is between 56-60 place directly at the bottom    
    elif (discard[0] >= 56):
        print('Computer has drawn a:', discard[0], 'from the discard pile')
        print(discard[0], 'has replaced', tower[9], 'in the computer tower')
        print('')
        find_and_replace(discard[0], tower[9], tower, discard)

    #follow scheme for accurately placing card within specified range of values
    for i in range(0,10):
        if (6*i < discard[0] <= 6*(i+1) and (tower[i] > 6*(i+1) or tower[i] < 6*i)):
            print('Computer has drawn a:', discard[0], 'from the discard pile')
            print(discard[0], 'has replaced', tower[i], 'in the computer tower')
            print('')
            find_and_replace(discard[0], tower[i], tower, discard)
            flag = 1
            return tower

    #if the card falls in a range where the tower already has a card, draw from the main pile
    if (flag == 0):
        brick = get_top_brick(main_pile)
        print('The computer has drawn a', brick, 'from the main pile')
        print('')

    #if that card falls within a range where the tower does not contain a card in that range, replace it
    for i in range(0,10):
        if (6*i < brick <= 6*(i+1) and (tower[i] > 6*(i+1) or tower[i] < 6*i)):
            print(brick, 'has replaced', tower[i], 'in the computer tower')
            print('')
            find_and_replace(brick, tower[i], tower, discard)
            flag1 = 1
            return tower

    #otherwise place drawn card in the discard pile
    if (flag1 == 0):
        add_brick_to_discard(brick, discard)
        print('The computer has placed', brick, 'in the discard pile')
        return tower

def choose_deck():
    '''Prompts the user which deck he/she would like to pick from.
       Main results in a draw from the main pile.
       Discard results in a draw from the discard pile.
       Any other response results in a reprompt for a valid resonse.'''

    #set global variables
    global main_pile
    global discard

    #set while loop flag
    c = 1

    while (c == 1):
        inp = input('Would you like to pick from the main or discard pile? ')

        if (inp == ''):
            print('Sorry, please enter a valid response ', 'help(choose_deck) for more information','',sep = '\n')
            continue
        
        elif (inp[0] == 'm' or inp[0] == 'M'):
            pile = main_pile
            c = 2
            
        elif (inp[0] == 'd' or inp[0] == 'D'):
            pile = discard
            c = 2
            
        else:
            print('Sorry, please enter a valid response ', 'help(choose_deck) for more information','',sep = '\n')
            continue
            
    return pile

def replace_brick():
    '''Prompts the user which brick he/she would like to replace.
       None results in placing the drawn pick in the discard pile.
       An integer between 0-60 will check to see if that brick is in the tower.
       Any other response will result in a reprompt.'''

    #set global variables
    global main_pile
    global discard

    #set while loop flag
    c = 1

    while (c == 1):
        inp = input('Which brick would you like to replace? ')

        if (inp == ''):
            print('Sorry, please enter a valid response ', 'help(replace_brick) for more information','',sep = '\n')
            continue
        
        elif (inp == 'none'):
            brick = inp
            c = 2
            break

        #checks to see if entry is an integer
        try:
            brick = int(inp)
        except ValueError as e:
            print('Please enter a valid integer', '\n')
            continue

        #if the value is within a valid range, exit the loop and return brick
        if (brick in range(0,61)):
            c = 2
            break

        else:
            print('Sorry, please enter a valid response ', 'help(choose_deck) for more information','',sep = '\n')
            continue
            
    return brick

def main():
    '''Main function that runs all subsequent functions and plays the game.'''

    #set initial flag
    flag = 0

    #setup game
    print_instructions()
    piles = setup_bricks()
    main_pile = piles[0]
    discard = piles[1]
    shuffle_bricks(main_pile)
    towers = deal_initial_bricks(main_pile)
    my_tower = towers[0]
    comp_tower = towers[1]
    main1 = get_top_brick(main_pile)
    add_brick_to_discard(main1, discard)

    #perform initial tower check
    check1 = check_tower_blaster(comp_tower)
    check2 = check_tower_blaster(my_tower)

    if (check1  == True):
        print('The game is over, computer has acheived a stable tower!', 'Player 2 loses :(', sep = '\n')

    elif (check2  == True):
        print('The game is over, user has acheived a stable tower!', 'Player 2 WINS :)', sep = '\n')

    print('Computer tower:', comp_tower, '\n' + 'Player tower:', my_tower,'\n')

    #while loop to run repeatedly run the game until a stable tower is achieved (ie. flag == 1)
    while (flag == 0):

        #simulate computer's move
        (main_pile, discard) = check_bricks(main_pile, discard)
        comp_tower = computer_play(comp_tower, main_pile, discard)

        #check to see if computer tower has achieved stability
        check1 = check_tower_blaster(comp_tower)
        if (check1  == True):
            print('The game is over, computer has acheived a stable tower!', 'Player 2 loses :(', sep = '\n')
            flag = 1
            break
        
        print('The top discard card is now:', discard[0], '\n')
        check_bricks(main_pile, discard)

        #prompt user to choose which deck to draw from
        select_pile = choose_deck()
        top = get_top_brick(select_pile)
        print('The brick you selected is:',top)
        b = 0

        #while loop to continuously prompt the user to specify which brick to replace until a valid response is chosen
        while (b == 0):
            old_brick = replace_brick()
            if (select_pile == discard and old_brick == 'none'):
                b = 1
                add_brick_to_discard(top, discard)
                break
            elif (find_and_replace(top, old_brick, my_tower, discard) == True):
                find_and_replace(top, old_brick, my_tower, discard)
                b = 1
            else:
                print('Please enter a valid choice for brick')
                print('')
                continue

        #check to see if user tower has achieved stability
        check2 = check_tower_blaster(my_tower)
        if (check2  == True):
            print('The game is over, user has acheived a stable tower!', 'Player 2 WINS :)', sep = '\n')
            flag = 1
            break
        
        print('The top discard card is now:', discard[0], '\n')
        print('Player tower:', my_tower,'\n')
        
    return

if (__name__ == '__main__'):
    main()
