import matplotlib.pyplot as plt
import math
import random
import time


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def heapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1   # left = 2*i + 1
    r = 2 * i + 2   # right = 2*i + 2

  # Проверяем существует ли левый дочерний элемент больший, чем корень

    if l < n and arr[i] < arr[l]:
        largest = l

    # Проверяем существует ли правый дочерний элемент больший, чем корень

    if r < n and arr[largest] < arr[r]:
        largest = r

    # Заменяем корень, если нужно
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # свап

        # Применяем heapify к корню.
        heapify(arr, n, largest)

# Основная функция для сортировки массива заданного размера
def heapSort(arr):
    n = len(arr)

    # Построение max-heap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # свап 
        heapify(arr, i, 0)

def sort(a):  
  for i in range(1, len(a)):
    if a[i] >  a[i-1]:
       a[i], a[i-1] = a[i-1], a[i]
    else:
      a[i], a[i-1] = a[i], a[i-1]
  return a

def bubble_sort(a):
  for i in range(len(a)):
    a = sort(a)
  return a

arrays = []
for len_ in range(0, 10000, 100):
    array = [random.randint(0, 10) for i in range(len_)]
    arrays.append(array)

time_algo = 0
times_quick_sort = []
for arr in arrays:
    start = time.time()
    quick_sort(arr)
    finish = time.time()
    time_algo = finish - start
    times_quick_sort.append(math.log2(time_algo))

time_algo = 0
times_heap_sort = []
for arr in arrays:
    start = time.time()
    heapSort(arr)
    finish = time.time()
    time_algo = finish - start
    times_heap_sort.append(math.log2(time_algo))

time_algo = 0
times_bubble_sort = []
for arr in arrays:
    start = time.time()
    bubble_sort(arr)
    finish = time.time()
    time_algo = finish - start
    times_bubble_sort.append(math.log2(time_algo))

arr_of_lens = [len(arr) for arr in arrays]
# print(bubble_sort([3,2,5,1]))

plt.figure(figsize = (10,10))
plt.plot(arr_of_lens, times_bubble_sort, label = 'bubble')
plt.plot(arr_of_lens, times_heap_sort, c = 'r', label = 'heap')
plt.plot(arr_of_lens, times_quick_sort, c = 'orange', label = 'quick_sort')
plt.legend()
plt.show()



