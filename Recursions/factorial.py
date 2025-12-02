import time


def factorial(n):
    product = 1
    for i in range(1, n + 1):
        product = product * i
    return product

def factorialRecursive(n):
    if n == 1:
        # base case
        return 1
    else:
        # recursive case
        return n * factorialRecursive(n - 1)
  
    
        
  
x = 999

start = time.time_ns()
print(factorial(x))
end = time.time_ns()
print(f"It took {end - start} to complete factorial, irritative way")

start = time.time_ns()
print(factorialRecursive(x))
end = time.time_ns()
print(f"It took {end - start} to complete factorial, recursive way")
