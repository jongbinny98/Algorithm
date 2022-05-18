import numpy as np
'''
insertion sort
To sort an array of size n in ascending order: 
1: Iterate from arr[1] to arr[n] over the array. 
2: Compare the current element (key) to its predecessor. 
3: If the key element is smaller than its predecessor,
   compare it to the elements before. 
   Move the greater elements one position up to make space for the swapped element.
Time complexity: O(n^2)
'''
def insertion_sort(arr):
    # range 1 ~ length of arr
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while j >= 0 and arr[j] > key:
            # basically arr[i] = arr[j] just that does not need to affect i
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

arr = np.array([1, 9, 5, 4, 3, 7, 2])
insertion_sort(arr)
for i in range(len(arr)):
    print(arr[i])