import threading

from ball import Ball
from player import Player

def name_generator(n, ball):
    for idx in range(n):
        yield ("Player " + str(idx+1), ball)

if __name__ == '__main__':
    print("start the game!")
    
    b = Ball()
    n_players = 5
    join_list = []
  
    for player_status in name_generator(n_players, b):
        thread = Player(player_status[0], player_status[1])
        thread.start()
        join_list.append(thread)

    for thread in join_list:
        thread.join()

    print("end game!")