from time import time

def compute_average(n):
    """Perform n appends to an empty list and return average time elapsed."""
    data = []
    start = time()
    for _ in range(n):
        data.append(None)
    end = time()
    return (end - start)/n

i = 100
while i <= 100000000:
    print(compute_average(i))
    i *= 10