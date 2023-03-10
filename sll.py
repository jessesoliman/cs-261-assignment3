# Name: Jesse Soliman
# OSU Email: solimaje@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 2/13/23
# Description: Implement a singly linked list data structure


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        Takes in a value and inserts a node of value 'value' at the front.
        """
        temp = self._head.next
        node_to_add = SLNode(value)
        self._head.next = node_to_add
        node_to_add.next = temp

    def insert_back(self, value: object) -> None:
        """
        Takes in a value and inserts a node of value 'value' in the back.
        """
        cur = self._head
        for i in range(self.length()):
            cur = cur.next
        node_to_add = SLNode(value)
        cur.next = node_to_add

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Takes in an index and value and inserts at index 'index' a node of
        value 'value'.
        """
        if index < 0 or index > self.length():
            raise SLLException
        cur = self._head
        for i in range(index):
            cur = cur.next
        temp = cur.next
        node_to_add = SLNode(value)
        cur.next = node_to_add
        node_to_add.next = temp

    def remove_at_index(self, index: int) -> None:
        """
        Takes in an index and removes the node at that index.
        """
        if index < 0 or index >= self.length():
            raise SLLException
        cur = self._head
        for i in range(index):
            cur = cur.next
        node_to_remove = cur.next
        cur.next = node_to_remove.next

    def remove(self, value: object) -> bool:
        """
        Takes in a value and removes the first node with value 'value'.
        """
        cur = self._head
        for i in range(self.length()):
            cur = cur.next
            if cur.value == value:
                self.remove_at_index(i)
                return True
        return False

    def count(self, value: object) -> int:
        """
        Takes in a value and returns the number of nodes of value 'value'.
        """
        counter = 0
        cur = self._head
        for i in range(self.length()):
            cur = cur.next
            if cur.value == value:
                counter += 1
        return counter

    def find(self, value: object) -> bool:
        """
        Takes in a value and returns true if a node of value 'value' exists.
        Returns false otherwise.
        """
        cur = self._head
        for i in range(self.length()):
            cur = cur.next
            if cur.value == value:
                return True
        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        Takes in a start index and a size. Returns a new linked list consisting
        of nodes of the subset indicated by the start index.
        """
        if (start_index < 0 or start_index >= self.length() or
                start_index + size > self.length() or size < 0):
            raise SLLException
        sliced_list = LinkedList()
        cur = self._head
        for i in range(start_index):
            cur = cur.next
        for i in range(size):
            cur = cur.next
            sliced_list.insert_back(cur.value)
        return sliced_list


if __name__ == "__main__":

    print("\n# insert_front example 1")
    test_case = ["A", "B", "C"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_front(case)
        print(lst)

    print("\n# insert_back example 1")
    test_case = ["C", "B", "A"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_back(case)
        print(lst)

    print("\n# insert_at_index example 1")
    lst = LinkedList()
    test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    for index, value in test_cases:
        print("Inserted", value, "at index", index, ": ", end="")
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove_at_index example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(f"Initial LinkedList : {lst}")
    for index in [0, 2, 0, 2, 2, -2]:
        print("Removed at index", index, ": ", end="")
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# remove example 2")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")
