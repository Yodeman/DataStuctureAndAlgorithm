from favoritesList import FavoritesList

class FavoritesListMTF(FavoritesList):
    """List of element ordered with move-to-front heuristic."""

    def _move_up(self, p):
        """Move accessed item at position p to front of list."""
        if p!=self._data.first():
            self._data.add_first(self._data.delete(p))

    def top(self, k):
        """Generate sequence of top k elements in terms of access count."""
        if not 1<=k<=len(self):
            raise ValueError("Illegal value for k")
        temp = PositionalList()
        for item in self._data:
            temp.add_last(item)

        for j in range(k):
            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            yield highPos.element()._value
            temp.delete(highPos)