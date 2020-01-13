# Ref: https://github.com/ZoranPandovski/al-go-rithms/tree/master/data_structures/trie


FOUND = "found"
NOT_FOUND = "not-found"


class TrieNode:
    def __init__(self,):
        self.children = [None] * 26  # English alphabets
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = self.get_new_node()

    def get_new_node(self):
        return TrieNode()

    def insert(self, word: str) -> None:
        new_trie_node = self.root
        length = len(word)

        for level in range(0, length):
            index = self._char_to_index(word[level])

            if not new_trie_node.children[index]:
                new_trie_node.children[index] = self.get_new_node()

            new_trie_node = new_trie_node.children[index]

        new_trie_node.is_end_of_word = True

    def search(self, word: str) -> str:
        new_trie_node = self.root
        length = len(word)

        for level in range(0, length):
            index = self._char_to_index(word[level])

            if not new_trie_node.children[index]:
                return NOT_FOUND

            new_trie_node = new_trie_node.children[index]

        if new_trie_node is not None and new_trie_node.is_end_of_word:
            return FOUND
        else:
            return NOT_FOUND

    def _char_to_index(self, char: str) -> int:
        index: int = ord(char) - ord("a")
        return index


def main() -> None:
    trie_node = Trie()
    words = ["the", "ah", "whoa"]

    for word in words:
        trie_node.insert(word)

    assert trie_node.search("the") == FOUND
    assert trie_node.search("who") == NOT_FOUND


if "__main__" == __name__:
    main()
