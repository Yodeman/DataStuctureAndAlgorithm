def isort(shelf):
    length = len(shelf)
    for i in range(1, length):
        hole = i
        while hole > 0 and shelf[i].size < shelf[hole - 1].size:
            hole = hole - 1
        shelf.insert(hole, shelf.pop(i))
    return

def insertion_sort(seq):
    """Sort list of comparable elements into nondecreasing order."""
    for k in range(1, len(seq)):
        cur = seq[k]            # current elements to be inserted.
        j = k
        while j > 0 and seq[j-1] > cur:
            #print(seq)
            seq[j] = seq[j-1]
            j -= 1
        seq[j] = cur

if __name__ =="__main__":
    seq = ['B', 'C', 'D', 'A', 'E', 'H', 'G', 'F']
    insertion_sort(seq)