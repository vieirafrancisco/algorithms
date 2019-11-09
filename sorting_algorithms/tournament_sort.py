import sys
import math
import random
import time

class TournamentSort:
    
    def __init__(self, arr):
        self.arr = arr
        self.arr_size = len(arr)
        self.depth = math.ceil(math.log2(self.arr_size))
        self.tree_arr =  (2 * pow(2,self.depth) - 1) * [sys.maxsize] # num_node(T) = num_leaf(n) + num_internal(n-1)

    def sort(self):
        sorted_arr = []
        self.set_leaves()
        while(len(sorted_arr) != self.arr_size): # O(n)
            begin = time.time()
            m, idx = self.min_heapify(0)
            end = time.time()
            print(end-begin)
            sorted_arr.append(m)
            self.tree_arr[idx] = sys.maxsize
        return sorted_arr

    def set_leaves(self):
        begin_leaf = int(pow(2, self.depth)) - 1
        leaves = range(begin_leaf, begin_leaf + self.arr_size)
        for i, j in enumerate(leaves):
            self.tree_arr[j] = self.arr[i]

    def min_heapify(self, idx): # O(log n)
        tree_size = len(self.tree_arr)
        left = 2 * idx + 1
        right = 2 * idx + 2
        if left >= tree_size or right >= tree_size: # O(1)
            return self.tree_arr[idx], idx

        val_l, idx_l = self.min_heapify(left)
        val_r, idx_r = self.min_heapify(right)
        if val_l < val_r:
            self.tree_arr[idx] = val_l
            return self.tree_arr[idx], idx_l
        else:
            self.tree_arr[idx] = val_r
            return self.tree_arr[idx], idx_r

if __name__ == '__main__':
    #t = TournamentSort([3,5,7,2])
    arr = [i for i in range(1000)]
    random.shuffle(arr)
    begin = time.time()
    t = TournamentSort(arr)
    sorted_arr = t.sort()
    end = time.time()
    print(end-begin)


    