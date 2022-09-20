'''Lunar Lander
Luke Kasper
36335048
I recieved assistance from the professor's office hours to correct an error I
had with repeating the game upon command
<5, 0, 5, 0, 5, 5, 0, 5, 10, 5, 15, 10, 10, 15, 10> => WIN
<0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0> => LOSS
'''
a = 1
#outer loop to restart the game on command
while (a == 1):               
    #set initial conditions
    b = 1
    altitude = 100 #[m]          
    velocity = 0.0 #[m/s]
    fuel = 100.0 #[L]
    t = 0 #[s]

    #loop to calculate parameters until the lunar lander reaches the ground (ie. alt = 0)
    while (altitude > 0):      

        #print parameters and prompt user for desired fuel burn after each second
        print('')
        print('Current alititude is: ', altitude, ' m', '\n', 'Current velocity is: ', velocity, ' m/s', '\n', 'Amount of fuel left is: ', fuel, ' L', '\n', sep = '')
        fuel_burn = input('Enter desired amount of fuel to burn: ')        

        #prevent user error from entering a non-number for fuel burn
        try:
            fuel_burn = float(fuel_burn)
        except ValueError as e:
            print('Please enter a valid number for fuel burn :)', '\n')
            continue
         
        #prevent negative fuel burn entry and negative total fuel
        if (fuel_burn <= 0):
            fuel_burn = 0
            fuel = fuel
        else:
            fuel = fuel - fuel_burn
    
        if (fuel <= 0):
            fuel = 0
        else:
            fuel = fuel       
        
        #calculate velocity, altitude, and time after each second
        velocity = velocity + 1.6 - 0.15*fuel_burn
        altitude = altitude - velocity   
        t += 1

    print('')
    print('~~~~~~~~~~~~GAME OVER~~~~~~~~~~~~~')
    print('Time to landing: ', t, ' seconds', '\n', 'Final velocity is: ', velocity, ' m/s', '\n', 'Amount of fuel left is: ', fuel, ' L', sep = '')   

    #criteria whether the landing was safe or a crash
    if (velocity <= 10):
        print('You safely landed on the moon!', '\n')
    else:
        print('So sorry but you crashed! :(', '\n')

    #loop to restart the game. Extra loop needed to reprompt the user if a non-valid response is entered.
    #entering n or N as a first letter exits both loops (invalidates both statements in while loops)
    #entering y or Y as a first letter exits just the inner while loop
    #entering any other letter as the first letter results in a reprompt and a message stating that it is not a valid response
    
    while (b == 1):
        inp = input('Would you like to play again? ')
        if (inp[0] == 'n' or inp[0] == 'N'):
            b = 2
            a = 2
        elif (inp[0] == 'y' or inp[0] == 'Y'):
            b = 2
        else:
            print('Sorry, please enter a valid response ', '\n')
            continue

    
