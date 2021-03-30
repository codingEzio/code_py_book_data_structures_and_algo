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

    def __len__(self):
        """
        O(N)
        """
        length = 0
        current_node = self.head

        # two scenarios
        #   directly return 0 if the Linked List is null (i.e. head=None)
        #   loop through via `next` to last element then stop (head=None)
        while current_node:
            length += 1
            current_node = current_node.next

        return length

    def __iter__(self):
        """
        O(N)
        """
        current_node = self.head

        while current_node:
            yield current_node

            # Just like a for/while loop but with a "stopper" in it (next-None)
            current_node = current_node.next

    def append(self, value):
        """
        O(N)
        """
        new_node = Node(value)

        # If there isn't anything at the beginning (i.e. a blank Linked List),
        # simply put this node in there (replace the dummy with this new node)
        if self.head is None:
            self.head = new_node
            return None

        # If there is something at the beginning, set the starting point there
        current_node = self.head

        # Loop the node to the last one, then assign the new node to its `next`
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def insert_before(self, index, value):
        """
        O(N)
        """
        if index < 0:
            return ValueError("Negative index is not yet supported")

        new_node = Node(value)

        # If the Linked List is null, simply put it there
        if self.head is None:
            self.head = new_node
            return None

        # If the Linked List isn't null (cuz it didn't return at the prev `if`)

        if index == 0:
            # move the `head` to the new node's `next`
            #   head(10, None) | new(20, None) => (20, head(10, None))
            #   you don't need to care about the rest of el since it's LinkedL
            new_node.next = self.head

            # set the new node as `head`
            #   head(10, None) -> head(20, 10)
            self.head = new_node

        else:
            # prepare to loop through this whole thing (Linked List)
            current_node = self.head
            current_index = 0

            while current_node:

                # find the node that before the node at the index (c -> c.next)
                if current_index == index - 1:

                    # there's only two nodes are involved
                    #   target_node         save the node we'll replace
                    #   current_node.next   precisely the node we'll replace
                    #   new_node.next       put saved node into new's `next`
                    target_node = current_node.next
                    current_node.next = new_node
                    new_node.next = target_node

                    return None

                current_index += 1
                current_node = current_node.next

        raise IndexError("SinglyLinkedList assignment index out of range")

    def pop(self, index):
        """
        O(N)
        """
        if index < 0:
            raise ValueError("Negative index is not yet supported")

        # if the index is 0, i.e. the `head` node
        if index == 0:
            deleted_value = self.head.value
            self.head = self.head.next
            return deleted_value

        # if the index is non-zero, we'll need to set `head` properly!
        else:
            # set the node to the "beginning" (excluding the 1st [0])
            previous_node = self.head
            current_node = self.head.next

            # set the index to its corresponding place (0 is catched by `if`)
            current_index = 1

            while current_node:
                if current_index == index:
                    # "delete" elem by shifting the elements forward
                    previous_node.next = current_node.next

                    # after "delete", return the element
                    deleted_value = current_node.value
                    return deleted_value

                # "delete" elem by shifting the elements forward
                previous_node = current_node

                # move towards the end (the last elem whose `next` is None)
                current_node = current_node.next
                current_index += 1

        raise IndexError("SinglyLinkedList deletion index out of range")

    def reverse(self):
        """
        O(N)
        """
        current_node = self.head
        previous_node = None

        while current_node:
            next_node = current_node.next

            current_node.next = previous_node
            previous_node = current_node

            current_node = next_node

        self.head = previous_node


def main():
    """
    Understanding of different parts
    - method `reverse`  meh
    - the rest of them  100%
    """
    pass


# references
#   examples only
#       https://github.com/vinta/fuck-coding-interviews/tree/master/data_structures/linked_lists
#   concept with examples
#       https://www.freecodecamp.org/news/python-interview-question-guide-how-to-code-a-linked-list-fd77cbbd367d/

if "__main__" == __name__:
    main()
