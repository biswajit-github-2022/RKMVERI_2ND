import DoublyLL

_DoublyLinkedBase=DoublyLL._DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):
    #-------------------------- nested Position class --------------------------
    class Position:
        def __init__(self,container,node) -> None:
            self.container=container
            self.node=node
        def element(self):
            return self.node._element
        def __eq__(self, other):
            """Return True if other is a Position representing the same locatio"""
            return type(other) is type(self) and other.node is self.node
        def __ne__(self, other):
            """Return True if other does not represent the same locatio"""
            return not(self == other)
    #------------------------------- utility method -------------------------------
    def _validate(self,p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be a proper Position type')
        if p.container is not self:
            raise ValueError('p does not belong to this container')
        if p.node._next is None:
            raise ValueError('p is no longer valid')
        return p.node
    def _make_position(self,node):
        """Return Position instance for given node (or None if sentinel"""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self,node)
    #------------------------------- accessors -------------------------------
    def first(self):
        return self._make_position(self._header._next)
    def last(self):
        return self._make_position(self._trailer._prev)
    def before(self,p):
        node=self._validate(p)
        return self._make_position(node._prev)
    def after(self,p):
        node=self._validate(p)
        return self._make_position(node._next)
    def __iter__(self):
        cursor=self.first()
        while cursor is not None:
            yield cursor.element()
            cursor=self.after(cursor)
    #------------------------------- mutators -------------------------------
    def _insert_between(self,e,predecessor,successor):
        node=super()._insert_between(e,predecessor,successor)
        return self._make_position(node)
    def add_first(self,e):
        return self._insert_between(e,self._header,self._header._next)
    def add_last(self,e):
        return self._insert_between(e,self._trailer._prev,self._trailer)
    def add_before(self,p,e):
        original=self._validate(p)
        return self._insert_between(e,original._prev,original)
    def add_after(self,p,e):
        original=self._validate(p)
        return self._insert_between(e,original,original._next)
    def delete(self,p):
        original=self._validate(p)
        return self._delete_node(original)
    def replace(self,p,e):
        original=self._validate(p)
        old_value=original._element
        original._element=e
        return old_value