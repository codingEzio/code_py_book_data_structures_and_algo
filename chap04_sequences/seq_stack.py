class Stack:
    """
    Visualize it as a "stack" of plates
    - you <push item(s) onto> the plates (first in, last out)
    - you <pop  item    off > the plates (last in, first out)
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(sum(self.items)) == 0

    def push(self, item):
        self.items.append(item)

    def top(self):
        if self.is_empty():
            raise RuntimeError("Attempt to get top of empty stack")

        top_index = len(self.items) - 1

        return self.items[top_index]

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Attempt to pop an empty stack")

        top_index = len(self.items) - 1
        top_item = self.items[top_index]

        del self.items

        return top_item


def main():
    pass


# references
#   concept
#       https://visualgo.net/en/list?slide=4

if "__main__" == __name__:
    main()
