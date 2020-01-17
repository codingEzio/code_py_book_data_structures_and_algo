# Ref: https://github.com/ZoranPandovski/al-go-rithms/tree/master/data_structures/heap/Python/BinaryHeaps

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
    """p.s. We have only implemented the most basic methods.
    """

    def __init__(self):
        self.array = [INFINITY]
        self.array_size = 0

    def insert(self, elem):
        self.array.append(elem)
        self.array_size += 1

        current_index = self.array_size

        while elem > self.array[self.parent(current_index)]:
            self.array[current_index], self.array[
                self.parent(current_index)
            ] = (
                self.array[self.parent(current_index)],
                self.array[current_index],
            )
            current_index = self.parent(current_index)

    def extract_max(self):
        """
        Delete and return the biggest element (root node).
        """
        root_node = self.get_root_node()

        self.array[1] = self.array.pop()
        self.array_size -= 1
        self._heapify(1)

        return root_node

    def _heapify(self, index):
        """
        This is the recursive method used in 'extract_max()'. It transform list
        into a heap in-place, the result should conform to the rules I've
        mentioned in the README file.
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
                self.array[index],
            )
            self._heapify(largest_index)


def main() -> None:
    hp = MaxHeap()

    hp.insert(10)
    hp.insert(40)
    hp.insert(50)
    hp.insert(20)
    hp.insert(70)
    hp.insert(110)
    hp.insert(30)
    hp.insert(1000)
    hp.insert(5)

    assert hp.extract_max() == 1000


if "__main__" == __name__:
    main()
