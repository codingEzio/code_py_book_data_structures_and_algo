class Queue:
    """
    First in, first out.

    Queue operations:
    - enqueue   enqueue(push) the item on the queue             O(1)
    - dequeue   returns the first enqueued item and removes it  O(1)
    - front     returns the first enqueued item                 O(1)
    """

    def __init__(self):
        self.items = []
        self.front_index = 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("Attempt to dequeue an empty queue")

        if self.front_index * 2 > len(self.items):
            self.__compress()

        item = self.items[self.front_index]
        self.front_index += 1

        return item

    def front(self):
        if self.is_empty():
            raise RuntimeError("Attempt to access front empty queue")

        item = self.items[self.front_index]

        return item

    def is_empty(self):
        return self.front_index == len(self.items)

    def __compress(self):
        new_list = []
        for idx in range(self.front_index, len(self.items)):
            new_list.append(self.items[idx])

        self.items = new_list
        self.front_index = 0


def main() -> None:
    qu = Queue()

    assert qu.is_empty() is True

    qu.enqueue(10)
    qu.enqueue(20)

    assert qu.front() == 10  # 10 remain unchanged
    assert qu.dequeue() == 10


if "__main__" == __name__:
    main()
