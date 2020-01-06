import hashset


class HashMap:
    # TODO Fully documenting this whole class.

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
        self.hash_set = hashset.HashSet()

    def __len__(self):
        return len(self.hash_set)

    def __contains__(self, item):
        return HashMap.__KVPair(key=item, value=None) in self.hash_set

    def not__contains__(self, item):
        return item not in self.hash_set

    def __setitem__(self, key, value):
        self.hash_set.add(HashMap.__KVPair(key=key, value=value))

    def __getitem__(self, key):
        if HashMap.__KVPair(key=key, value=None) in self.hash_set:
            val = self.hash_set[HashMap.__KVPair(key, None)].get_value()
            return val

        raise KeyError(f"Key {str(key)} not in HashMap")

    def __iter__(self):
        for n in self.hash_set:
            yield n.get_key()


def main() -> None:
    pass


if "__main__" == __name__:
    main()
