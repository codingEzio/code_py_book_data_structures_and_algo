
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
        self.first = LinkedList.__Node(None, None)
        self.last = self.first
        self.num_items = 0

        for cont in contents:
            self.append(cont)
