#Recursively reverse a sequence

def reverse(seq, start, stop):
    """Reverse elements in implicit slice seq[start:stop]"""
    if start < stop-1:
        seq[start], seq[stop-1] = seq[stop-1], seq[start]
        reverse(seq, start+1, stop-1)