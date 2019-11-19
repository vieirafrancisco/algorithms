import sys
import math
import random
import time

from element import Element

INF = sys.maxsize

class TournamentSort:
    
    def __init__(self, arr):
        self.arr = arr
        self.arr_size = len(arr)
        self.depth = math.ceil(math.log2(self.arr_size))
        self.tree_arr =  (2 * pow(2,self.depth) - 1) * [Element(INF)]

    def sort(self):
        sorted_arr = []
        self.set_leaves()
        self.build_tree(0)
        
        while(len(sorted_arr) != self.arr_size): # O(nlogn)
            sorted_arr.append(self.tree_arr[0])
            last_leaf = pow(2,self.depth) - 1
            i = 0
            while(i < last_leaf):
                if self.tree_arr[i] == self.tree_arr[2*i + 1]:
                    i = 2*i + 1
                else:
                    i = 2*i + 2
            self.tree_arr[i] = Element(INF)

            while(i > 0): # O(2*logn) == O(logn)
                parent = math.ceil(i/2)-1
                f_child = i
                if i % 2 == 0: s_child = i-1
                else: s_child = i+1

                if self.tree_arr[f_child] < self.tree_arr[s_child]:
                    self.tree_arr[parent] = self.tree_arr[f_child]
                else:
                    self.tree_arr[parent] = self.tree_arr[s_child]
                i = parent

        return sorted_arr

    def set_leaves(self):
        begin_leaf = int(pow(2, self.depth)) - 1
        leaves = range(begin_leaf, begin_leaf + self.arr_size)
        for i, j in enumerate(leaves):
            self.tree_arr[j] = self.arr[i]

    def build_tree(self, idx): # O(n)
        tree_size = len(self.tree_arr)
        left = 2 * idx + 1
        right = 2 * idx + 2
        if left >= tree_size and right >= tree_size: # O(1)
            return self.tree_arr[idx]
        self.tree_arr[idx] = min(self.build_tree(left), self.build_tree(right))
        return self.tree_arr[idx]

if __name__ == '__main__':
    arr = [Element(i) for i in range(100)]
    random.shuffle(arr)
    begin = time.time()
    t = TournamentSort(arr)
    sorted_arr = t.sort()
    end = time.time()
    print(end-begin)
    print(sorted_arr)
    num_comparations = 0
    for element in sorted_arr:
        num_comparations += element.num_comparations
    print(num_comparations)