# Требования по методам: вставка и удаление (O(1)), длина (O(1))

from collections import deque

class Queue:
    """ FIFO array: append at the end and remove and the start of array """

    def __init__(self):
        self.store = deque()

    def enqueue(self, element):
        self.store.append(element)

    def dequeue(self):
        self.store.popleft()  # O (N)

    def __len__(self):
        return len(self.store)


storage = Queue()
storage.enqueue(1)
storage.enqueue(2)
storage.dequeue()
print(storage.store)

