from DSandALGO.linkedlist.doublyLL import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements alloing positional access."""

    class Position:
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this position."""
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not(self==other)

    def _validate(self, p):
        """Return position's node or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        """Return position instance for given node(or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Return position just before position p(or None if p is first)."""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Return position just after position p (or None if p is last)."""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
    
    def _insert_between(self, element, predecessor, successor):
        node = super()._insert_between(element, predecessor, successor)
        return self._make_position(node)
    
    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element e into list after position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        """
        Replace the element at position p with e.
        Return the element formerly at position p
        """
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value