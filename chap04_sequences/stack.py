class Stack:
    """
    Last in, first out.

    Stack operations:
    - push          push the item on the stack              O(1)
    - pop           returns the top item and removes it     O(1)
    - top           returns the top item                    O(1)
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Attempt to pop an empty stack")

        top_index = len(self.items) - 1
        item = self.items[top_index]

        del self.items[top_index]

        return item

    def top(self):
        if self.is_empty():
            raise RuntimeError("Attempt to get top of empty stack")

        top_index = len(self.items) - 1
        item = self.items[top_index]

        return item

    def is_empty(self):
        return len(self.items) == 0


def main() -> None:
    st = Stack()

    assert st.is_empty() is True

    st.push(10)
    st.push(20)

    assert st.top() == 20  # 20 remain unchanged
    assert st.pop() == 20


if "__main__" == __name__:
    main()
