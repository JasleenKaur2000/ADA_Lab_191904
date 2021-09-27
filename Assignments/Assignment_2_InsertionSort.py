import numpy as np
import time

def insertionSort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key


n=int(input("Enter the size of array:"))
arr=np.random.rand(n)
start=time.time()
insertionSort(arr)
end=time.time()
print(arr)
print(end-start)