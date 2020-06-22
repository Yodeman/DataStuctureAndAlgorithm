def binary_search(data, target, low=0, high=0):
    """Return True if target is found in indicated portion of a Python list."""
    #data = data.sort()
    if high == 0:
        high = len(data)-1

    if low > high:
        return False
    else:
        mid = (low+high)/2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)