#

def bubble_sort(array):
    x = len(array)

    for i in range(x):
        for j in range(0, x-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j+ 1], array[j]

array = [10, 1, 4, 6, 7, 8]

bubble_sort(array)