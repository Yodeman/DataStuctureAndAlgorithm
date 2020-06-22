def binary_sum(seq, start, stop):
    """Return the sum of the numbers in implicit slice seq[start:stop]."""
    if start >= stop:
        return 0
    elif start == stop-1:
        return seq[start]
    else:
        mid = (start+stop)//2
        return binary_sum(seq, start, mid) + binary_sum(seq, mid, stop)