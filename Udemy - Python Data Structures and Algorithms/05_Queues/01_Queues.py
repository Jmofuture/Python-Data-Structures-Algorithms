class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length =+ 1


    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next



    def enqueue(self, value):

        new_node = Node(value)

        if self.length is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1


    def dequeue(self):
        
        if self.length is None:
            return
        


my_queue = Queue(37)

my_queue.print_queue()

my_queue.enqueue(35)

my_queue.print_queue()