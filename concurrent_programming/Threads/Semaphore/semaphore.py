import random

class Semaphore:

    def __init__(self):
        self.__mutex = 1
        self.__active = False
        self.__sleep_list = []

    def down(self, thread):
        if self.__mutex == 0:
            print(thread.get_name(), "tried to get the ball, sleeping!")
            self.__sleep_list.append(thread)
            #print(self.__sleep_list)
            thread.sleep()
        else:
            self.__mutex -= 1
            self.__active = True
            print(thread.get_name(), "has the ball!")
            #print(self.__sleep_list)

    def up(self):
        if self.has_someone_sleeping():
            list_size = len(self.__sleep_list)
            rand_index = random.randint(0, list_size-1)
            curr_thread = self.__sleep_list[rand_index]
            self.__sleep_list.remove(curr_thread)
            curr_thread.wakeup()
            #print(self.__sleep_list)
        self.__mutex = 1
        self.__active = False

    def is_active(self):
        if self.__active:
            return True
        else:
            return False

    def is_sleeping(self, thread):
        if thread in self.__sleep_list:
            return True
        else:
            return False

    def has_someone_sleeping(self):
        if self.__sleep_list != []:
            return True
        else:
            return False