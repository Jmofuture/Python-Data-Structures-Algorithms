class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 



class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1



    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next


    def push(self, value):

        new_node = Node(value)

        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1


    def pop(self):
        if self.height == 0:
            return None
         
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        
        return temp

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list) 

    def size(self):
        return len(self.stack_list)


def sort_stack(stack):
    if stack is None or stack.is_empty():
        return stack

    temp_stack = Stack()

    while not stack.is_empty():

        temp = stack.pop()

        while not temp_stack.is_empty() and temp_stack.peek() > temp:
            stack.push(temp_stack.pop())

        temp_stack.push(temp)

    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return stack




my_stack = Stack(37)

my_stack.push(33)
my_stack.push(2)
my_stack.push(23)




my_stack.pop()


my_stack.print_stack()