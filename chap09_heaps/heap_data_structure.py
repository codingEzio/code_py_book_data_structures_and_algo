from math import inf as INFINITY


class Heap:
    """
    Parent class for MaxHeap and MinHeap.
    """

    def get_root_node(self):
        if self.array_size > 0:
            return self.array[1]
        else:
            return self.array[0]

    def get_array(self):
        return self.array[1:]

    @staticmethod
    def parent(index):
        return index // 2

    @staticmethod
    def child_left(index):
        return index * 2

    @staticmethod
    def child_right(index):
        return index * 2 + 1

    def is_child_left(self, index):
        return self.child_left(index) < len(self.array)

    def is_child_right(self, index):
        return self.child_right(index) < len(self.array)


class MaxHeap(Heap):
    def __init__(self):
        self.array = [INFINITY]
        self.size = 0

    def insert(self, elem):
        self.array.append(elem)
        self.array_size += 1

        current_index = self.array_size

        BISECTED_INDEX = self.parent(current_index)
        while elem > self.array[BISECTED_INDEX]:
            self.array[current_index], self.array[BISECTED_INDEX] = (
                self.array[BISECTED_INDEX],
                self.array[current_index],
            )
            current_index = BISECTED_INDEX

    def pop_max(self):
        """
        Delete and return the biggest element (root node).
        """
        root_node = self.get_root_node()

        self.array[1] = self.array.pop()
        self.size -= 1
        self.max_heapify(1)

        return root_node

    def heapify(self, index):
        """
        Transform list into a heap in-place, the transformed result should conform the
        rules I've mentioned in the notes.
        """
        largest_index = index

        if (
            self.is_child_left(index)
            and self.array[self.child_left(index)] > self.array[largest_index]
        ):
            largest_index = self.child_left(index)

        if (
            self.is_child_right(index)
            and self.array[self.child_right(index)] > self.array[largest_index]
        ):
            largest_index = self.child_right(index)

        if largest_index != index:
            self.array[index], self.array[largest_index] = (
                self.array[largest_index],
                self.array[index]
            )
            self.heapify(largest_index)
