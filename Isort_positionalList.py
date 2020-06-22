from DSandALGO.positionalList.positionallist import PositionalList

def insertion_sort(L):
    """Sort PoaitionalList of comparable elements into nondecreasing order."""

    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value > marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)

if __name__ == "__main__":
    L = PositionalList()
    for num in [15, 22, 25, 29, 36, 23, 53, 11, 42]:
        L.add_last(num)
    insertion_sort(L)
    for i in L:
        print(i, end=" ")