from __future__ import annotations
from typing import List, Union, Iterator, Optional

IntOrNone = Optional[int]
IntIteratorOrNone = Optional[Iterator[int]]
IntList = List[int]
IntOrNoneList = List[Union[int, None]]


class PyList:
    """
    For the sake of simplicity, this class only supports int lists.
    """

    def __init__(self, contents: IntList = [], size: int = 10):
        self.items: IntOrNoneList = [None] * size
        self.num_items: int = len(self.items)
        self.size: int = size

        cont: int
        for cont in contents:
            self.append(cont)

    def __makeroom(self):
        """Increase list size when the original one is full."""
        new_len = (self.size // 4) + self.size + 1
        new_lst = [None] * new_len
        idx: int

        for idx in range(self.num_items):
            new_lst[idx] = self.items[idx]

        self.items = new_lst
        self.size = new_len

    def append(self, item) -> None:
        if self.num_items == self.size:
            self.__makeroom()

        self.items[self.num_items] = item
        self.num_items = self.num_items + 1

    def __iter__(self) -> IntIteratorOrNone:
        for item in self.items:
            yield item

    def __getitem__(self, index: int) -> IntOrNone:
        if index >= 0 and index < self.num_items:
            return self.items[index]
        raise IndexError("PyList index out of range.")

    def __setitem__(self, index: int, val: int) -> None:
        if index >= 0 and index < self.num_items:
            self.items[index] = val
            return None
        raise IndexError("PyList assignment index out of range.")

    def __add__(self, other: PyList) -> PyList:
        idx: int
        result: PyList = PyList(size=self.num_items + other.num_items)

        for idx in range(self.num_items):
            result.append(self.items[idx])

        for idx in range(other.num_items):
            result.append(other.items[idx])

        return result
