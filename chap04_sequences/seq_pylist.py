class PyList:
    def __init__(self, contents=[], size=10):
        """
        O(1) if no value is passed
        O(N) if a sequence is passed to the constructor

        num_items   number of actual items (or (mem)locations)
        size        the space being allocated/initialized (don't mind the 10)
        """
        self.items = [None] * size
        self.num_items = 0
        self.size = size

        for item in contents:
            self.append(item)

    def __getitem__(self, index):
        """
        O(1)
        """
        if index >= 0 and index < self.num_items:
            return self.items[index]

        # make the sure the index is in the range of acceptable indices
        raise IndexError("PyList accessing index out of range")

    def __setitem__(self, index, value):
        """
        O(1)
        """
        if index >= 0 and index < self.num_items:
            self.items[index] = value
            return None

        # make the sure the index is in the range of acceptable indices
        raise IndexError("PyList assignment index out of range")

    def __delitem__(self, index):
        """
        O(N)
        """
        for idx in range(index, self.num_items - 1):
            # kinda like the reverse shifting of 'insert'
            # move anything after `idx` forward by one item
            self.items[idx] = self.items[idx + 1]

        self.num_items -= 1

    def __eq__(self, other):
        """
        O(N)
        """

        # different type
        if type(other) != type(self):
            return False

        # different size
        if self.num_items != other.num_items:
            return False

        # one-by-one comparison
        for idx in range(self.num_items):
            if self.items[idx] != other.items[idx]:
                return False

        return True

    def __contains__(self, item):
        """
        O(N)
        """
        for idx in range(self.num_items):
            if self.items[idx] == item:
                return True

        return False

    def __add__(self, other):
        """
        O(N)
        """

        # it doesn't mutate either list; it builds a new one
        result = PyList(size=self.num_items + other.num_items)

        for idx in range(self.num_items):
            result.append(self.items[idx])

        for idx in range(other.num_items):
            result.append(other.num_items[idx])

        return result

    def __len__(self):
        """
        O(1)
        """
        return len(self.num_items)

    def __iter__(self):
        """
        O(N)
        """
        for idx in range(self.num_items):
            yield self.items[idx]

    def __str__(self):
        """
        ready for functions like `print`
        """
        s = "["

        for idx in range(self.num_items):
            s = s + repr(self.items[idx])

            if idx < self.num_items - 1:
                s = s + ", "

        s = s + "]"

        return s

    def __repr__(self):
        """
        ready for functions like `eval` (eval(PyList()) -> initilization)
        """
        s = "PyList(["

        for idx in range(self.num_items):
            s = s + repr(self.items[idx])

            if idx < self.num_items - 1:
                s = s + ", "

        s = s + "])"

        return s

    def __make_room(self):
        """
        dynamically increase the size of the list
        only executed when the room (non-None slot) is almost full
        """

        # the '4' is chosen arbitrarily (but it's quite efficient)
        new_len = (self.size // 4) + self.size + 1
        new_lst = [None] * new_len

        for idx in range(self.num_items):
            new_lst[idx] = self.items[idx]

        self.items = new_lst
        self.size = new_len

    def append(self, item):
        """
        O(1)
        """
        if self.num_items == self.size:
            self.__make_room()

        self.items[self.num_items] = item
        self.num_items += 1

    def insert(self, idx, item):
        """
        O(N)
        """
        if self.num_items == self.size:
            self.__make_room()

        if idx < self.num_items:
            # move the elements behind lst[idx] by one element
            for i in range(self.num_items - 1, i - 1, -1):
                self.items[i + 1] = self.items[i]

            # set the value for the new item
            self.items[idx] = item
            self.num_items += 1
        else:
            # simply add to the end if `idx` is bigger than crt size
            self.append(item)


def main():
    # sample_list = PyList(["a", "b", "c"])
    # print(sample_list[0])
    pass


if "__main__" == __name__:
    main()
