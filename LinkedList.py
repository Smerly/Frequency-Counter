from Node import Node
# from collections import Counter


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def find(self, item):
        current = self.head
        counter = 0

        while current != None:

            if current.data[0] == item:
                return counter
            else:
                current = current.next
                counter += 1
        return -1

    def length(self):
        if self.head == None:
            return 0
        else:
            counter = 1
            current = self.head
            while(current.next):
                current = current.next
                counter += 1
            return counter

    # def update(self, key, value):

    #     current = self.head

    #     found = False
    #     counter = 0

    #     while current != None and not found:

    #         if current.data[0] == key:
    #             # counter += 1
    #             # current = current.next
    #             current.data = (current.data[0], current.data[1]+1)
    #             # current.data = (current.data[0], current.data[1])
    #         else:
    #             current = current.next
    #             counter += 1
    #     # return counter

    def put(self, item):
        current = self.head
        if current:
            while current:
                if current.data[0] == item:
                    current.data = (current.data[0], current.data[1] + 1)
                    return
                current = current.next
        self.append((item, 1))

    def print_nodes(self):
        current = self.head

        if current != None:
            for i in range(self.length()):
                print(f' {current.data[0]} : {current.data[1]}')
                current = current.next
