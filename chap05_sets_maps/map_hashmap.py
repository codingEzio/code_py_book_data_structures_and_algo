from map_hashset import HashSet


class HashMap:
    """
    It has many faces(names), including map, dictionary, and hash tables.

    Status for this class:
    - barely understood, since I haven't even finish documented the `HashSet`.
    - start to work through this class after you finish the `HashSet`!
        - or you could read and code other implementations :)
    """

    class __KVPair:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __eq__(self, other):
            if type(self) != type(other):
                return False

            return self.key == other.key

        def get_key(self):
            return self.key

        def get_value(self):
            return self.value

        def __hash__(self):
            return hash(self.key)

    def __init__(self):
        self.hashset = HashSet()

    def __len__(self):
        return len(self.hashset)

    def __contains__(self, item):
        return HashSet.__KVPair(item, None) in self.hashset

    def __setitem__(self, key, value):
        self.hashset.add(HashMap.__KVPair(key, value))

    def __getitem__(self, key):
        if HashMap.__KVPair(key, None) in self.hashset:
            value = self.hashset[HashMap.__KVPair(key, None)].get_value()

            return value

        raise KeyError(f"Key {str(key)} not in HashMap")

    def __iter__(self):
        for item in self.hashset:
            yield item.get_key()


def main():
    pass


if "__main__" == __name__:
    main()
