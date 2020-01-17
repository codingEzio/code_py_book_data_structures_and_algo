# Ref: https://github.com/keon/algorithms/blob/master/algorithms/heap/binary_heap.py


class MinHeap:
    def __init__(self):
        self.current_size = 0
        self.heap = [(0)]

    def insert(self, value):
        self.heap.append(value)
        self.current_size = self.current_size + 1
        self._perc_up(self.current_size)

    def remove_min(self):
        min_elem = self.heap[1]
        self.heap[1] = self.heap[self.current_size]
        self.current_size = self.current_size - 1
        self.heap.pop()
        self._perc_down(1)
        return min_elem

    def _perc_up(self, idx):
        """I still have no idea about what 'perc' stands for.
        """
        while idx // 2 > 0:
            if self.heap[idx] < self.heap[idx // 2]:
                self.heap[idx], self.heap[idx // 2] = (
                    self.heap[idx // 2],
                    self.heap[idx],
                )
            idx = idx // 2

    def _perc_down(self, idx):
        """I still have no idea about what 'perc' stands for.
        """
        while idx * 2 < self.current_size:
            min_child = self.__min_child(idx)

            if self.heap[min_child] < self.heap[idx]:
                self.heap[min_child], self.heap[idx] = (
                    self.heap[idx],
                    self.heap[min_child],
                )

            idx = min_child

    def __min_child(self, idx):
        if idx * 2 + 1 > self.current_size:
            return idx * 2
        else:
            if self.heap[idx * 2] > self.heap[idx * 2 + 1]:
                return idx * 2 + 1
            else:
                return idx * 2


def main() -> None:
    hp = MinHeap()

    hp.insert(10)
    hp.insert(40)
    hp.insert(50)
    hp.insert(20)
    hp.insert(70)
    hp.insert(110)
    hp.insert(30)
    hp.insert(1000)
    hp.insert(5)

    assert hp.remove_min() == 5


if "__main__" == __name__:
    main()
