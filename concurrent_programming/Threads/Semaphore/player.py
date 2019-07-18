import time
import threading

class Player(threading.Thread):
    
    def __init__(self, name, ball):
        super().__init__(name=name)
        self.name = name
        self.ball = ball
        self.was_sleeping = False
        self.__wake = True

    def run(self):
        self.ball.get_the_ball(self)

    def sleep(self):
        self.was_sleeping = True
        self.__wake = False
        while(not self.__wake):
            time.sleep(1)

    def wakeup(self):
        print(self.name, "wakeup!", self.was_sleeping)
        self.__wake = True

    def get_name(self):
        return self.name