import numpy as np
import time

def bubbleSort(arr):
    n = len(arr)
 
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

n=int(input("Enter the size of array:"))
arr=np.random.rand(n)
start=time.time()
bubbleSort(arr)
end=time.time()
print(arr)
print(end-start)