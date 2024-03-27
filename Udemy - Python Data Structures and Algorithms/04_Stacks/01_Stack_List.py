class Stack:
    def __init__(self):
        self.stack_list = []


    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])


    def is_empty(self):
        return len(self.stack_list) == 0


    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]


    def size(self):
        return len(self.stack_list)


    def push(self, value):
        self.stack_list.append(value)


    def pop(self):
        if self.is_empty():
            return
        else:
            return self.stack_list.pop()    
        





def is_balanced_parentheses(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty() or stack.pop() != '(':
                return False
    return stack.is_empty()






#WRITE REVERSE_STRING

def reverse_string(string):

    if string != '':
        return string[::-1]
    else:
        return ''
    

"""
The sort_stack function takes a single argument, a Stack object.  
The function should sort the elements in the stack in ascending order 
(the lowest value will be at the top of the stack) using only one additional stack. 

"""


def sort_stack(stack):

    if stack is None:
        return stack.is_empty()
    

    values = []
    new_stack = Stack()
