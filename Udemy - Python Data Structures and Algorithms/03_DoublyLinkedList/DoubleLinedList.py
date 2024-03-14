class Node: #Constructor de nodos
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList: #constructor de Listas
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
        

    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.tail

        if self.length == 1:
            self.head = None 
            self.tail = None  
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        
        self.length -= 1
        return temp        
        

    def prepend(self, value):

        new_node = Node(value)
        
        if self.length == 0:
            self.head = new_node 
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.length += 1

        return True

    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head

        if self.length == 1: 

            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None 
        self.length -= 1
        
        return temp    


    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head

        if index < self.length/2:
            for _ in range(index):
                temp = temp.next

        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev

        return temp


    def set_value(self, index, value):
        temp = self.get(index)

        if temp:
            temp.value = value
            return True
        return False


    def insert(self, index, value):

        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)    

        if index == self.length:
            return self.append(value)  
        
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True


    def remove(self, index):

        if index < 0 or index > self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            return self.pop()
        

        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next

        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp


    def print_list(self):
        if self.length == 0:
            return None
        
        temp = self.head

        while temp:
            print(temp.value)
            temp = temp.next
        
    def swap_first_last(self):
        if self.length < 2:  
            return

        self.head.value = self.tail.value
        self.tail.value = self.head.value


    def reverse(self):
        if self.length < 2:
            return

        current = self.head
        
        while current:
            temp = current.next
            current.next = current.prev
            current.prev = temp
        
            current = temp

        self.head = self.tail
        self.tail = self.head
        
        return True


    def is_palindrome(self):
        if self.length is None or self.length < 2:
            return True
        
        nums = []
        current = self.head

        while current:
            nums.append(current.value)
            current = current.next

        reverse_nums = nums[::-1]

        return nums == reverse_nums
        

    def swap_pairs(self):
        if self.length is None or self.length < 2:
            return      
        
        dummy = Node(0)
        dummy.next = self.head
        current = dummy

        while current.next and current.next.next:
            first = current.next
            second = current.next.next


            first.next = second.next
            second.next = first
            current.next = second

    
            current = first


        self.head = dummy.next



l = DoublyLinkedList(37)

l.append(1)
l.append(1)
l.append(1)
l.append(1)
l.append(37)



print(l.is_palindrome())

l.print_list()