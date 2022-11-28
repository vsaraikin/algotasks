class Node:

    def __init__(self, val: int, prev: 'Node' = None, next: 'Node' = None):

        self.next = next
        if self.next:
            self.next.prev = self

        self.val = val

        self.prev = prev
        if self.prev:
            self.prev.next = self


class MyCircularQueue:

    def __init__(self, k: int):
        self.beg = None
        self.end = None
        self.__length = 0
        self.k = k
        

    def enQueue(self, value: int) -> bool:
        
        if self.isFull():
            return False
        
        else:
        
            if self.end:
                self.end = Node(value, self.end)
            else:
                self.beg = self.end = Node(value)
            self.__length += 1
            return True


    def deQueue(self) -> bool:
        if self.beg:
            self.beg = self.beg.next
            if not self.beg:
                self.end = None
            self.__length -= 1
            
            return True
        else:
            return False

    def Front(self) -> int:
        if self.beg:
            return self.beg.val
        else:
            return -1
    
    
    def Rear(self) -> int:
        if not self.beg:
            return -1
        else:
            next = self.beg
            val = next.val
            while next.val is not None:
                val = next.val
                next = next.next
                if not next: 
                    break

            return val

    def isEmpty(self) -> bool:
        if self.__length != 0:
            return False
        else:
            return True

    def isFull(self) -> bool:
        if self.__length >= self.k:
            return True
        else:
            return False
        
        
    def traverse(self):
        
        if self.beg:
            print(self.beg.val)
            
            next = self.beg.next
            
            while next:
                print(next.val)
                next = next.next     


myCircularQueue = MyCircularQueue(8)
myCircularQueue.enQueue(4); # return True
myCircularQueue.enQueue(9); # return True
myCircularQueue.deQueue();  # return True
myCircularQueue.deQueue();  # return True
myCircularQueue.traverse()
print(myCircularQueue.isEmpty())