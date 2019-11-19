# https://en.wikipedia.org/wiki/Selection_sort
# Complexity O(n^2)
import time
import random

from element import Element

def swap(arr: list, a: int, b: int) -> None:
    arr[a], arr[b] = arr[b], arr[a]

def selection_sort(arr: list) -> list:
    tmp_arr = arr.copy()
    n = len(tmp_arr)
    
    for i in range(n):
        m = tmp_arr[i]
        m_idx = i
        for j in range(i, n):
            if tmp_arr[j] < m:
                m = tmp_arr[j]
                m_idx = j
        swap(tmp_arr, i, m_idx)

    return tmp_arr

if __name__ == '__main__':
    arr = [Element(i) for i in range(1000)]
    random.shuffle(arr)
    begin = time.time()
    result_arr = selection_sort(arr)
    end = time.time()
    print(end-begin)
    num_comparations = 0
    for element in result_arr:
        num_comparations += element.num_comparations
    print(num_comparations)