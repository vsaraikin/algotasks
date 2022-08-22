class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        """ Print all elements in list """
        element = self.head

        while element:
            print(element.data)
            if element.data is None:
                break
            element = element.next

    def push_first(self, new_element: Node):
        """ Insert Node before at the start of list """
        new_element.next = self.head
        self.head = new_element

    def push_last(self, new_element: Node):
        """ Append Node at the end of list """
        element = self.head

        while element:
            if element.next is None:
                element.next = new_element
                break
            element = element.next

    def insert(self, new_element: Node, position: int):
        """ Insert Node at a given index """
        i = 0
        element = self.head
        while position <= i:
            i += 1
            element = element.next

        new_element.next = element.next
        element.next = new_element

    def remove(self, position: int):
        """ Remove Node by index """
        i = 1
        element = self.head

        while position != i:
            i += 1
            element = element.next  # element = prev_node before deleting

        prev_element = element
        element_to_delete = prev_element.next
        prev_element.next = element_to_delete.next


linked_list = LinkedList()
linked_list.head = Node(1)
linked_list.push_last(Node(2))
linked_list.push_last(Node(4))
linked_list.push_last(Node(5))
# linked_list.insert(Node(5), 1)
linked_list.remove(2)
linked_list.__str__()
