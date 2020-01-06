class HashSet:
    # TODO Fully documenting this whole class.

    class __Placeholder:
        def __init__(self):
            pass

        def __eq__(self, other):
            return False

    def __init__(self, contents=[]):
        self.items = [None] * 10
        self.num_items = 0

        for cont in contents:
            self.add(cont)

    def add(self, item):
        if HashSet.__add(item, self.items):
            self.num_items += 1
            load = self.num_items / len(self.items)
            if load >= 0.75:
                self.items = HashSet.__rehash(
                    old_list=self.items, new_list=[None] * 2 * len(self.items)
                )

    def remove(self, item):
        if HashSet.__remove(item=item, items=self.items) is True:
            self.num_items -= 1
            load = max(self.num_items, 10) / len(self.items)
            if load <= 0.25:
                self.items = HashSet.__rehash(
                    old_list=self.items,
                    new_list=[None] * int(len(self.items) / 2),
                )
        else:
            raise KeyError("Item not in HashSet")

    def difference_update(self, other):
        for item in other:
            self.discard(item)

    def difference(self, other):
        result = HashSet(self)
        result.difference_update(other)
        return result

    @staticmethod
    def __add(item, items):
        idx = hash(item) % len(items)
        loc = -1

        while items[idx] is not None:
            if items[idx] == item:
                return False

            if loc < 0 and type(items[idx]) == HashSet.__Placeholder:
                loc = idx

            idx = (idx + 1) % len(items)

        if loc < 0:
            loc = idx

        items[loc] = item

    @staticmethod
    def __remove(item, items):
        idx = hash(item) % len(items)

        while items[idx] is not None:
            if items[idx] == item:
                next_idx = (idx + 1) % len(items)

                if items[next_idx] is None:
                    items[idx] = None
                else:
                    items[idx] = HashSet.__Placeholder()

                return True

            idx = (idx + 1) % len(items)

        return False

    @staticmethod
    def __rehash(old_list, new_list):
        for n in old_list:
            if n is not None and type(n) != HashSet.__Placeholder:
                HashSet.__add(item=n, items=new_list)

        return new_list

    def __getitem__(self, item):
        idx = hash(item) % len(self.items)

        while self.items[idx] is not None:
            if self.items[idx] == item:
                return self.items[idx]

            idx = (idx + 1) % len(self.items)

        return None

    def __iter__(self):
        for i in range(len(self.items)):
            if (
                self.items[i] is not None
                and type(self.items[i]) != HashSet.__Placeholder
            ):
                yield self.items[i]

    def __contains__(self, item):
        idx = hash(item) % len(self.items)

        while self.items[idx] is not None:
            if self.items[idx] == item:
                return True

            idx = (idx + 1) % len(self.items)

        return False


def main() -> None:
    pass


if "__main__" == __name__:
    main()
