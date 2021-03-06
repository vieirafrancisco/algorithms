import time
import random
import threading

from semaphore import Semaphore


class Ball:

    def __init__(self):
        self.time_count = 0
        self.sem = Semaphore()

    def get_the_ball(self, thread):
        while(self.time_count < 45):
            self.sem.down(thread) # down

            if thread.was_sleeping:
                thread.was_sleeping = False
            else:
                # CRITICAL REGION
                time.sleep(random.randint(1, 2)) # min 1 sec / max 2 sec
                
                # Leave critical region
                self.left_the_ball(thread)
                self.time_count += 1
        
        if not self.sem.is_active() and self.sem.has_someone_sleeping():
            self.sem.up()

    def left_the_ball(self, thread):
        print(thread.get_name(), "left the ball!")
        self.sem.up() # up
        time.sleep(random.randint(1, 2))
