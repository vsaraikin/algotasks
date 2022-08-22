class Stack:
    """ LIFO array: push and pop from the tail of array """

    def __init__(self):
        self.store = []

    def push(self, element):
        self.store.append(element)

    def pop(self):
        self.store.pop()

    def __len__(self):
        pass


storage = Stack().store
storage.append(1)
storage.append(2)
storage.pop()
print(storage)
