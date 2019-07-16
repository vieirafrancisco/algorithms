import time
import random
import threading

from semaphore import Semaphore

class Ball:

    def __init__(self):
        self.time_count = 0
        self.sem = Semaphore()

    def get_the_ball(self, name, thread):
        while(self.time_count < 10):
            self.sem.down(thread) # down
            print(name, "has the ball!")
            time.sleep(random.randint(1, 4) / 2) # min 0.5 sec / max 2 sec
            self.left_the_ball(name, thread)
            self.time_count += 1

    def left_the_ball(self, name, thread):
        print(name, "left the ball!")
        self.sem.up(thread) # up
        time.sleep(random.randint(1, 4) / 2)