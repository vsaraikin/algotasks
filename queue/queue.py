class Queue:
    """ FIFO array: append at the end and remove and the start of array """

    def __init__(self):
        self.store = []

    def enqueue(self, element):
        self.store.append(element)

    def dequeue(self):
        self.store.pop(0)  # O (N)

    def __len__(self):
        pass


storage = Queue()
storage.enqueue(1)
storage.enqueue(2)
storage.dequeue()
print(storage.store)

