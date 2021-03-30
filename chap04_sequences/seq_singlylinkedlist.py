class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    """
    There are LOTS of different implementations, each with different levels of
    completeness. Here's just a basic example for Singly Linked List :P
    """

    def __init__(self, head=None):
        """
        Nothing special with the `head`, it just represents the first node.
        """
        self.head = head

    def __len__(self):
        pass

    def index(self, value):
        """
        O(N)
        """

        # set the starting point (one more meta info than seqs like list)
        current_index = 0
        current_node = self.head

        # eventually it'd reach the last item (which its `next` is None)
        while current_node:

            # compare one by one with the value of the instance
            if current_node.value == value:
                return current_index

            # push this loop closer to its end (a ?fancier version of `+= 1`)
            current_node = current_node.next

            # keep in sync with the state of finding (no-return -> maybe next?)
            current_index += 1

        raise ValueError(f"{value} is not in this Linked List")

    def __getitem__(self, index):
        """
        O(N)
        """
        if index < 0:
            raise ValueError("Negative index is not yet supported")

        # much like the `index` method, only at this time we want its value
        current_index = 0
        current_node = self.head

        # if did not find anywhere in the Linked List, raise an error
        while current_node:

            # return immediately if the request element is at the beginning
            if current_index == index:
                return current_node.value

            # move forward (ref to the next node, corresponding index)
            else:
                current_node = current_node.next
                current_index += 1

        raise IndexError("SinglyLinkedList accessing index out of range")

    def __setitem__(self, index, value):
        """
        O(N)
        """
        if index < 0:
            raise ValueError("Negative index is not yet supported")

        current_index = 0
        current_node = self.head

        while current_node:

            if current_index == index:

                # overwritten if there's already data inside
                current_node.value = value

                return None

            current_node = current_node.next

            # move the slider towards the index specified
            current_index += 1

        raise IndexError("SinglyLinkedList assignment index out of range")

    def __iter__(self):
        pass

    def insert_before(self):
        pass

    def append(self):
        pass

    def pop(self):
        pass

    def reverse(self):
        pass


def main():
    pass


# references
#   examples only
#       https://github.com/vinta/fuck-coding-interviews/tree/master/data_structures/linked_lists
#   concept with examples
#       https://www.freecodecamp.org/news/python-interview-question-guide-how-to-code-a-linked-list-fd77cbbd367d/

if "__main__" == __name__:
    main()
