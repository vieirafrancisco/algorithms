import concurrent.futures
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
  
    for player in name_generator(n_players, b):
        thread = Player(player[0], player[1])
        thread.start()
        join_list.append(thread)

    for thread in join_list:
        thread.join()    

#     t1 = Player("Player 1", b)
#     t2 = Player("Player 2", b)
#     t3 = Player("Player 3", b)

#     t1.start()
#     t2.start()
#     t3.start()

#     t1.join()
#     t2.join()
#     t3.join()

    # context manager to start and end the thread
    #with concurrent.futures.ThreadPoolExecutor(max_workers=n_players) as player:
    #    player.map(b.get_the_ball, name_generator(n_players))

    print("end game!")