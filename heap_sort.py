
class HeapSort:
    def __init__(self):
        self.arr = None
        self.size = 0

    def sort(self, arr):
        self.arr = arr
        self.size = len(arr)

        for i in range(self.size-1, -1):
            self.heapify(i)
        
        for i in range(1, self.size):
            self.swap(0, self.size-i)
            self.heapify(0, self.size-i-1)

    def heapify(self, i, n):
        left = 2 * i + 1
        right = 2 * i + 2
        greatest = i

        if left < n and self.arr[left] > self.arr[i]:
            greatest = left
        if right < n and self.arr[right] > greatest:
            greatest = right

        if greatest != i:
            self.swap(i, greatest)
            self.heapify(greatest)

    def swap(self, x, y):
        self.arr[x], self.arr[y] = self.arr[y], self.arr[x]


if __name__ == '__main__':
    pass