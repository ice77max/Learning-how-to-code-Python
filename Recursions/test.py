def myRecursion(n):
    print(f"{n=}")
    if n == 1:
        print("Base case reached")
        return
    else:
        myRecursion(n - 1)
        print(f"{n=} while n * n = {n * n}")
        return
myRecursion(5)