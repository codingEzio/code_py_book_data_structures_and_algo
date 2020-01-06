# Rename this file to 'linkedlist_stackabus' before you push to Github

__doc__ = """Basics
  Array is
  - not dynamic, memory has to be allocated in advance
  - difficult(slow) to insert|remove an item (need to update a large num of items)
  - able to directly access an item (aka. random accessible list)
  - memory allocation mechanism: pre-allocate, fixed-size-at-least-when-init

  Linked List is
  - dynamic, no memory is allocated before the node was added
  - easy to insert|delete items spince it wasn't stored in a contiguous location
  - suitable for implementing lists, stacks, queues :)
  - not able to directly access an item (need to "loop" to the location)
  - memory allocation mechanism: allocate-when-needed, extra-memory-for-ref-tothenext
"""


class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None  # aka. `next` in other implementations


class LinkedList:
    def __init__(self):
        """
        1st  node -> point to next (real) item
        last node -> half data, half ref to None (a cond to stop)
        """
        # Explanations of common-used statements
        # >> node.ref                        right(next item), left(next is ?)
        # >> self.start_node                 no item (point to 1st real one)
        # >> node = self.start_node          giving a start to loop through
        # >> new_node.ref = self.start_node  the next(ref) item is RIGHT_SIDE
        self.start_node = None

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return None
        else:
            all_nodes = []
            node = self.start_node
            while node is not None:
                all_nodes.append(node.item)
                node = node.ref  # ref: ref to the next item
            return all_nodes

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.start_node is None:
            self.start_node = new_node
            return None

        node = self.start_node

        while node.ref is not None:
            node = node.ref

        node.ref = new_node

    def insert_after_item(self, existing_item, data):
        node = self.start_node
        # print(f"{node.ref}")

        # Loop to the location we wanna insert into (unlike list XD)
        while node is not None:
            if node.item == existing_item:
                break
            node = node.ref

        if node is None:
            print("item is not in the list")
        else:
            new_node = Node(data)
            new_node.ref = node.ref
            node.ref = new_node

    def insert_before_item(self, existing_item, data):
        # No element at all
        if self.start_node is None:
            print("List has no element")
            return None

        # Only has one element
        if self.start_node.item == existing_item:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return None

        node = self.start_node
        # print(f"{node.ref}")

        while node.ref is not None:
            if node.ref.item == existing_item:
                break
            node = node.ref

        if node.ref is None:
            print("item is not in the list")
        else:
            new_node = Node(data)
            new_node.ref = node.ref
            node.ref = new_node

    def insert_at_index(self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node

        i = 1
        node = self.start_node

        # Loop the node to the (index-1)th place
        while i < index - 1 and node is not None:
            node = node.ref
            i = i + 1

        if node is None:
            print("Index out of bound")
        else:
            new_node = Node(data)
            new_node.ref = node.ref
            node.ref = new_node

    def get_count(self):
        if self.start_node is None:
            return 0

        node = self.start_node
        count = 0

        while node is not None:
            count = count + 1
            node = node.ref

        return count

    def search_item(self, existing_item):
        """Return a boolean value to indicates whether found or not."""
        if self.start_node is None:
            print("List has no elements")
            return None

        node = self.start_node

        while node is not None:
            if node.item == existing_item:
                # print("Item found")
                return True

            node = node.ref

        # print("Item not found")
        return False

    def make_new_list_via_user_input(self):
        numbers = int(input(">> How many nodes do you wanna create: "))
        if numbers == 0:
            return None
        for i in range(numbers):
            value = int(input(">> Enter the value for the node: "))
            self.insert_at_end(value)

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return None

        # Make the next(ref) item as the start (not start_node but 1st one)
        self.start_node = self.start_node.ref

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return None

        node = self.start_node

        # Loop towards the end till the penultimate one (the last ref is None)
        while node.ref.ref is not None:
            node = node.ref

        # Assign None to ref(next) of the penultimate item (=> del last item)
        node.ref = None

    def delete_item_by_value(self, existing_item):
        if self.start_node is None:
            print("The list has no element to delete")
            return None

        if self.start_node.item == existing_item:
            self.start_node = self.start_node.ref
            return None

        node = self.start_node

        # Loop the point where the next item would be the one you wanna del
        while node.ref is not None:
            if node.ref.item == existing_item:
                break
            node = node.ref

        # Now the node should be at where the node you wanna delete (U, DEL)

        # Didn't found anything after looping all the way through (-> end)
        if node.ref is None:
            print("Item not found in the list")
        # e.g. delete 2 from [1,2,3], it's [1.next <- 1.next.next]
        else:
            node.ref = node.ref.ref


def main():
    """Use debugger or pythontutor.com to see the detailed procedures"""
    ll = LinkedList()

    # All three different scenarios
    ll.insert_at_end(5)
    ll.insert_at_end(10)
    ll.insert_at_end(15)

    ll.insert_at_start(1)

    ll.insert_after_item(10, 13)
    ll.insert_before_item(13, 11)

    ll.insert_at_index(5, 12)

    assert ll.get_count() == 7
    assert ll.search_item(5) is True

    # ll.make_new_list_via_user_input()
    assert ll.traverse_list() == [1, 5, 10, 11, 12, 13, 15]

    ll.delete_at_start()
    assert ll.traverse_list() == [5, 10, 11, 12, 13, 15]

    ll.delete_at_end()
    assert ll.traverse_list() == [5, 10, 11, 12, 13]

    ll.delete_item_by_value(11)
    assert ll.traverse_list() == [5, 10, 12, 13]


if __name__ == "__main__":
    main()
