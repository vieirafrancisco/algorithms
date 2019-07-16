import random

class Semaphore:

    def __init__(self):
        self.__mutex = 1
        self.__sleep_list = []

    def down(self, thread):
        if self.__mutex == 0:
            self.__sleep_list.append(thread)
            thread.sleep()
        else:
            self.__mutex -= 1

    def up(self, thread):
        if self.__sleep_list != []:
            list_size = len(self.__sleep_list)
            rand_index = random.randint(0, list_size-1)
            curr_thread = self.__sleep_list[rand_index]
            self.__sleep_list.remove(curr_thread)
            self.__mutex = 1
            curr_thread.wakeup()

    def is_sleeping(self, thread):
        if thread in self.__sleep_list:
            return True
        else:
            return False