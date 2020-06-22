def factorial(n):
    if n == 0:          #if n < 2:
        return 1
    else:
        return n * factorial(n-1)