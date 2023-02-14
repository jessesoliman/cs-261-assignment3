# Name: Jesse Soliman
# OSU Email: solimaje@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 2/13/2023
# Description: Implement a Queue ADT class using a chain of Singly-Linked
#              Nodes as the underlying storage.


from SLNode import SLNode


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Initialize new queue with head and tail nodes
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'QUEUE ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        Add a node of value 'value' to the end of the queue (self._tail).
        """
        if self._head is not None:
            cur = self._head
            for i in range(self.size()-1):
                cur = cur.next
            previous_last = self._tail
            self._tail = SLNode(value)
            previous_last.next = self._tail
        else:
            self._head = SLNode(value)
            self._tail = self._head

    def dequeue(self) -> object:
        """
        Remove the node at the front of the queue(self._head) and return
        its value.
        """
        if self.is_empty() is True:
            raise QueueException
        dequeued_node = self._head.value
        self._head = self._head.next
        return dequeued_node

    def front(self) -> object:
        """
        Return the value at the front of the queue(self._head.value).
        """
        if self.is_empty() is True:
            raise QueueException
        return self._head.value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))

    print('\n#front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)
