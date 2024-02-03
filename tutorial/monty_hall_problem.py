'''
What is the best startegy for the 
for let's make a deal?
'''

import random
import matplotlib.pyplot as plt
DOORCNT = 5


def play_game(swtch):
    doors = list(range(1,DOORCNT + 1))

    #Assign a winning door at random
    car = random.choice(doors)
    #print(f'The car is behind door number: {car}')

    #Player chooses a door at random
    plyr_choice = random.choice(doors)
    doors.remove(plyr_choice)
    #print(f'The player chose door number {plyr_choice}')
    
    #host removes one of the doors
    #THAT IS NOT THE CAR
    non_car_doors = doors.copy()
    if car != plyr_choice:
        non_car_doors.remove(car)
    goat = random.choice(non_car_doors)
    #print(f'The host opened door number {goat} to reveal a goat')
    
    #Player doesnt switch 
    if swtch:
        #The player cant pick the same door twice      
        doors.remove(goat)        
        plyr_choice = random.choice(doors)
        #print(f' The player switched their choice to {plyr_choice}')
        
    if car == plyr_choice:
        #print('The player won!')
        #Player won
        return 1
    else:
        #print('The player lost')
        #Player lost
        return 0
def get_win_pcnt(gm_cnt, switch):
    nswp = []
    ns_wins = 0
    for i in range(1,gm_cnt+1):
        #Play game and get win percentage
        ns_wins += play_game(switch)
        nswp.append((ns_wins/i)*100)   
    return nswp
         
def long_term_games(gm_cnt):
    x = list(range(1,gm_cnt+1))
    nswp = get_win_pcnt(gm_cnt, False)
    print(nswp[-1])
    plt.plot(x, nswp, label='not switching')
    swp = get_win_pcnt(gm_cnt, True)
    print(swp[-1])
    plt.plot(x, swp, label='switching')
    plt.xlabel( 'Number of games')
    plt.ylabel ( 'Win percentage')
  
    plt.legend()
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    long_term_games(20000)