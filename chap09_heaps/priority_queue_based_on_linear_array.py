# Ref: https://github.com/keon/algorithms/blob/master/algorithms/queues/priority_queue.py

import itertools


class PriorityQueueNode:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

    def __repr__(self):
        return f"{self.data}: {self.priority}"


class PriorityQueue:
    """An implementation of priority queue using linear array.
    """

    def __init__(self, items=None, priorities=None):
        self.priority_queue_list = []

        if items is None:
            return None
        if priorities is None:
            priorities = itertools.repeat(None)

        for item, priority in zip(items, priorities):
            self.push(item, priority=priority)

    def __repr__(self):
        return f"PriorityQueue<{repr(self.priority_queue_list)}>"

    def size(self):
        return len(self.priority_queue_list)

    def push(self, item, priority=None):
        """
        Push the item into the priority queue.

        If priority is not given, priority is set to the value of item.
        Then the comparison will kinda be like 'John < Alisa' (not accurate!).
        """
        priority = item if priority is None else priority
        pq_node = PriorityQueueNode(item, priority)

        for idx, current in enumerate(self.priority_queue_list):
            if current.priority < pq_node.priority:
                self.priority_queue_list.insert(idx, pq_node)

                return None

        self.priority_queue_list.append(pq_node)

    def pop(self):
        """Remove and return the item with the lowest priority.
        """
        return self.priority_queue_list.pop().data


def main() -> None:
    items = ["John", "Alisa"]
    priorities = [29, 20]

    pq = PriorityQueue(items=items, priorities=priorities)

    pq.push(item="Bobby", priority=23)

    assert str(pq) == "PriorityQueue<[John: 29, Bobby: 23, Alisa: 20]>"
    assert pq.size() == 3
    assert pq.pop() == "Alisa"


if "__main__" == __name__:
    main()
