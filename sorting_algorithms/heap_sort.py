import time
import random

from element import Element

class HeapSort:
    def __init__(self, arr):
        self.arr = arr.copy()
        self.size = len(arr)

    def sort(self):
        for i in range(self.size, -1, -1):
            self.heapify(i, self.size)

        for i in range(self.size - 1, 0, -1):
            self.swap(0, i)
            self.heapify(0, i)
        return self.arr

    def heapify(self, i, n):
        left = 2 * i + 1
        right = 2 * i + 2
        greatest = i

        if left < n and self.arr[left] > self.arr[i]:
            greatest = left
        if right < n and self.arr[right] > self.arr[greatest]:
            greatest = right

        if greatest != i:
            self.swap(i, greatest)
            self.heapify(greatest, n)

    def swap(self, x, y):
        self.arr[x], self.arr[y] = self.arr[y], self.arr[x]


if __name__ == '__main__':
    
    arr = [Element(i) for i in range(1000000)]
    random.shuffle(arr)
    begin = time.time()
    hs = HeapSort(arr)
    sorted_arr = hs.sort()
    end = time.time()
    print(end-begin)
    num_comparations = 0
    for element in hs.arr:
        num_comparations += element.num_comparations
    print(num_comparations)
