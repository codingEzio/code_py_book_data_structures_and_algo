class Queue:
    """
    Visualize it as "people getting into line at a counter"
    - people <enqueue> into the line   (first came   ~ first in, first out)
    - people <dequeue> out of the line (first served ~ last in, last out)
    """

    def __init__(self):
        self.items = []
        self.front_index = 0

    def is_empty(self):
        return len(self.items) == self.front_index

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("Ateempt to dequeue an empty queue")

        front_item = self.items[self.front_index]
        self.front_index += 1

        return front_item

    def front(self):
        if self.is_empty():
            raise RuntimeError("Ateempt to accesss of empty queue")

        return self.items[self.front_index]


def main():
    pass


# references
#   concept
#       https://visualgo.net/en/list?slide=5
#       https://www.reddit.com/r/learnprogramming/comments/2yha59/queues_vs_stacks/cp9tq77/

if "__main__" == __name__:
    main()
