import time
import random
import threading

from semaphore import Semaphore

class Ball:

    def __init__(self):
        self.time_count = 0
        self.sem = Semaphore()

    def get_the_ball(self, name, thread):
        while(self.time_count < 3):
            print(self.time_count, thread.get_name())
            self.sem.down(thread) # down

            if thread.was_sleeping:
                thread.was_sleeping = False
            else:
                # CRITICAL REGION
                time.sleep(random.randint(1, 2)) # min 1 sec / max 2 sec
                
                # Leave critical region
                self.left_the_ball(name, thread)
                self.time_count += 1

    def left_the_ball(self, name, thread):
        print(name, "left the ball!")
        self.sem.up(thread) # up
        time.sleep(random.randint(1, 2))