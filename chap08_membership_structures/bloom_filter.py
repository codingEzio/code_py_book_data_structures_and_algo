# Ref: https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/

# dev
import math
import mmh3
from bitarray import bitarray

# test
from random import shuffle
import crayons


class BloomFilter:
    def __init__(self, items_count, fp_prob):
        self.fp_prob = fp_prob
        self.size = self.get_size(items_count, fp_prob)
        self.hash_count = self.get_hash_count(self.size, items_count)
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)

    def add(self, item):
        """Add an item to the filter.
        """
        digests = []

        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            digests.append(digest)

            self.bit_array[digest] = True

    def check(self, item):
        """Check whether an item exists in the filter.
        """
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size

            if self.bit_array[digest] == False:
                return False

        return True

    @classmethod
    def get_size(self, items_count, fp_prob):
        """The size of the bit array.
        """
        m = -(items_count * math.log(fp_prob)) / (math.log(2) ** 2)
        return int(m)

    @classmethod
    def get_hash_count(self, bitarr_size, items_count):
        """Optimum number of hash functions.
        """
        k = (bitarr_size / items_count) * math.log(2)
        return int(k)


def main() -> None:
    n = 20
    fp_prob = 0.05
    bloom_filter = BloomFilter(items_count=n, fp_prob=fp_prob)

    print("-" * 40)
    print(f"Num of hash functions     : {bloom_filter.hash_count}")
    print(f"Size of the bit array     : {bloom_filter.size}")
    print(f"False positive probability: {bloom_filter.fp_prob}")
    print("-" * 40)

    # terminal color
    RED = crayons.red
    BLUE = crayons.blue
    GREEN = crayons.green

    # fmt: off
    word_present = [
        "abound", "abounds", "abundance", "abundant", "accessable",
        "bloom", "blossom", "bolster", "bonny", "bonus",
        "bonuses", "coherent", "cohesive", "colorful", "comely",
        "comfort", "gems", "generosity", "generous", "generously",
        "genial",
    ]
    word_absent = [
        "bluff", "cheater", "hate", "war", "humanity",
        "racism", "hurt", "nuke", "gloomy", "facebook",
        "geeksforgeeks", "twitter",
    ]

    for item in word_present:
        bloom_filter.add(item)

    shuffle(word_present)
    shuffle(word_absent)

    test_words = word_present[:10] + word_absent
    shuffle(test_words)

    for word in test_words:
        if bloom_filter.check(word):
            if word in word_absent:
                print(f"{word} is a {BLUE('false positive')}!")
            else:
                print(f"{word} is {GREEN('probably present')}.")
        else:
            print(f"{word} is definitely {RED('not present')}!")


if "__main__" == __name__:
    main()
