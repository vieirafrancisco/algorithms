import time
import random

class HeapSort:
    def __init__(self):
        self.arr = None
        self.size = 0

    def sort(self, arr):
        self.arr = arr.copy()
        self.size = len(arr)

        for i in range(self.size, -1, -1):
            self.heapify(i, self.size)

        for i in range(self.size - 1, 0, -1):
            self.swap(0, i)
            self.heapify(0, i)

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
    hs = HeapSort()
    arr = [i for i in range(1000000)]
    random.shuffle(arr)
    begin = time.time()
    hs.sort(arr)
    end = time.time()
    print(end-begin)