def countDownAnUp(n):
    print(n)
    if n == 0:
        # Base case
        print("Reached the base case.")
        return
    else:
        # recursive case
        countDownAnUp(n -1)
        print(n, "returning")
        return
countDownAnUp(2)
