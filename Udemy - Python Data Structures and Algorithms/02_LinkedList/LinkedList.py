
"""

head = {
            "value":11,
            "next":{
                    "value":3,
                    "next": {
                            "value":23,
                            "next":{
                                    "value":7,
                                    "next":{
                                            "value":4,
                                            "next":None
                                    }
                            }
                    }

            }


}

print(head["next"]["next"]["value"])

"""

#Clase que genera nuevos nodos

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
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
            self.tail = new_node
        self.length += 1 
        return True #Es opcional, para poder se llamado por otro metodo
    
    def pop(self):
        if self.head is None: #Si está vacia la lista
            return None
            # Dos o mas nodos
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0: #Un solo nodo 
            self.head = None
            self.tail = None
        return temp


    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    
    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None 
        self.length -= 1
        
        if self.length == 0:
            self.tail = None
        return temp


    def get(self, index):
        if index < 0 or index >= self.length:
            return None 
        temp = self.head 
        for _ in range(index):
            temp = temp.next
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
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    

    def remove(self, index):

        if index < 0 or index > self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            return self.pop() 
        
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp


    def reverse(self):

        temp = self.head

        self.head = self.tail
        self.tail = temp

        after = self.head.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


#ejercicios - Al mover uno dos veces mas raido que el orto cuando fast llega al final, slow va por el medio
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

#
    def has_loop(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False


    def partition_list(self, x):

        if self.head is None:
            return None
        
        dummy1 = Node(0) #Mantienen el inicio de lista
        dummy2 = Node(0)

        prev1 = dummy1
        prev2 = dummy2

        current = self.head

        while current:
            if current.value < x:
                prev1.next = current
                prev1 = prev1.next

            else:
                prev2.next = current
                prev2.next 
        
        current = current.next


        prev1.next = dummy2.next
        prev2.next = None

        self.head = dummy1.next
        return dummy1

    def remove_duplicates(self):
        if self.head is None:
            return None    
            
        current = self.head
        seen = set([current.value])
        while current.next:
            
            if current.next.value in seen:
                current.next = current.next.next 
            else:
                seen.add(current.next.value)
                current = current.next


    def binary_to_decimal(self):
        if self.head is None:
            return 0
    
        temp = self.head
        temp_list = []

        while temp is not None:
            temp_list.append(temp.value)
            temp = temp.next
        
        decimal = 0
    
        for i, value in enumerate(reversed(temp_list)):
            decimal += value * (2 ** i)
    
        return decimal

    def reverse_between(self, start_index, end_index):
        if not self.head or start_index == end_index:
            return

        dummy = Node(0)
        dummy.next = self.head
        prev = dummy


        for _ in range(start_index):
            prev = prev.next


        current = prev.next
        for _ in range(end_index - start_index):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp

        if start_index == 0:
            self.head = dummy.next
        

my_linked_list = LinkedList(4)





my_linked_list.append(37)
my_linked_list.append(3)
my_linked_list.append(7)
my_linked_list.append(10)
my_linked_list.append(17)
my_linked_list.append(24)
my_linked_list.append(20)
my_linked_list.append(20)
my_linked_list.append(20)
my_linked_list.append(20)




#my_linked_list.print_list()

#print("Valor medio: ",my_linked_list.find_middle_node().value)

#print("Pruna con head/tail",my_linked_list.head.value)




def find_kth_from_end(linkedlist, k):

    head = linkedlist.head
    value_list = []

    while head is not None:
        value_list.append(head)
        head = head.next

    reversed_list = value_list[::-1]

    print(reversed_list)
    #print(reversed_list.value)

    max_k =  len(reversed_list)
    min_k =  1     

    if value_list is None:
        return None
    if k < min_k or k > max_k:
        print("El numero debe ser entre 1 y", max_k)
        return None
    if k == (max_k + 1):
        result = reversed_list[0]
        print(reversed_list[0])
    else:
        result = reversed_list[((k)-1)]
        print(result)
    return result
    


    

#find_kth_from_end(my_linked_list, 8)

  # Output: 4

my_linked_list.print_list()

my_linked_list.remove_duplicates()

my_linked_list.print_list()