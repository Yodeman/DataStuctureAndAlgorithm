#Recursively sum all the range element of a sequence using linear recursion.
def linear_sum(seq, n):
    """Return the sum of the first n element of the seq."""
    if n==0:
        return 0
    else:
        return linear_sum(seq, n-1) + seq[n-1]