#Program 1 to write fibonaaci series and study its time complexity for varying inputs.

def fib(n):
    n1, n2 = 0, 1
    count = 0
    while count < n:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1



x=int(input("Enter the number:"))
fib(x)