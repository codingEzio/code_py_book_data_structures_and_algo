class LinkedList:
    """Serves a different purpose in comparison to built-in list."""

    # Inviside to the outside (by using two underscores)
    class __Node:
        def __init__(self, item, next=None):
            """
            One node has two parts, one is the value itself (item),
            the other half points/references to the next node (next).
            """
            self.item = item
            self.next = next

        def get_item(self):
            return self.item

        def get_next(self):
            return self.next

        def set_item(self, item):
            self.item = item

        def set_next(self, next):
            self.next = next

    def __init__(self, contents={}):
        # Both point to a dummy node to begin with (alway the 1st, no `item`(val))
        self.first = LinkedList.__Node(None, None)
        self.last = self.first

        self.num_items = 0

        for cont in contents:
            self.append(cont)

    def append(self, item):
        """
        Each append will always take the same amount of time (O(1)).
        But of course, it also takes up twice the spce of a random accessible
        list since there has to be room for both the refs to {item, next node}.
        """
        node = LinkedList.__Node(item)
        self.last.set_next(node)
        self.last = node
        self.num_items += 1

    def insert(self, index, item):
        """
        Suits for doing many inserts near the beginning of a list.

        Either inserts into the specified location (with O(ELEM_BEFORE)),
        or simply append to the end of the list (with O(1)).

        Two scenarios where the complexity would be O(1)
        - insert at the beginning of a list
        - the index is greater than current size (therefore append)
        """
        cursor = self.first

        if index < self.num_items:
            for i in range(index):
                cursor = cursor.get_next()

            node = LinkedList.__Node(item, cursor.get_next())
            cursor.set_next(node)
            self.num_items += 1
        else:
            self.append(item)

    def __getitem__(self, index):
        """
        Impractical impl (O(N)). Use list if random access is desired.
        Linked lists require linear search to access a particular location.
        """
        if index >= 0 and index < self.num_items:
            cursor = self.first.get_next()
            for i in range(index):
                cursor = cursor.get_next()

            return cursor.get_item()

        raise IndexError("LinkedList index out of range (get)")

    def __setitem__(self, index, val):
        """
        Impractical impl (O(N)). Use list if random access is desired.
        Linked lists require linear search to access a particular location.
        """
        if index >= 0 and index < self.num_items:
            cursor = self.first.get_next()
            for i in range(index):
                cursor = cursor.get_next()

            cursor.set_item(val)
            return None

        raise IndexError("LinkedList assignment out of range (set)")

    def __add__(self, other):
        """
        Given [1, 3] & [2, 0], excepts [1, 3, 2, 0], aka "concatenation".
        """
        # Don't use fixed isinstance(X, CLS), it'd fail if being imported.
        if type(self) != type(other):
            raise TypeError(
                f"Concatenate undefined for "
                f"{str(type(self))} + {str(type(other))}"
            )

        result = LinkedList()

        # Skip the 1st element as there's no value inside (`item`)
        cursor_self = self.first.get_next()

        while cursor_self is not None:
            result.append(cursor_self.get_item())
            cursor_self = cursor_self.get_next()

        # Skip the 1st element as there's no value inside (`item`)
        cursor_other = other.first.get_next()

        while cursor_other is not None:
            result.append(cursor_other.get_item())
            cursor_other = cursor_other.get_next()

        return result
