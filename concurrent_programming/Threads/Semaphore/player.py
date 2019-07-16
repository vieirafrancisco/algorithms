import threading

class Player(threading.Thread):
    def __init__(self, name, ball):
        super().__init__(name=name)
        self.name = name
        self.ball = ball
        self.event = threading.Event()

    def run(self):
        self.ball.get_the_ball(self.name, self)

    def sleep(self):
        self.event.wait()

    def wakeup(self):
        self.event.set()

    def is_sleeping(self):
        if self.event.is_set():
            return True
        else:
            return False