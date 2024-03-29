class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None 

#Se crea el arbol vacio root apuntara al primer Nodo 

class BinarySearchTree:
    def __init__(self):
        self.root = None #Apunta al primer Nodo

    
    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True

        temp = self.root

        while True:
            if new_node.value == temp.value:
                return False

            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right    


    
    def contains(self, value):

        temp = self.root

        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
            
        return False 
    

my_tree = BinarySearchTree()

my_tree.insert(37)
my_tree.insert(33)
my_tree.insert(40)
my_tree.insert(57)
my_tree.insert(2)
my_tree.insert(13)
my_tree.insert(33)
my_tree.insert(33)



print(my_tree.root.value)
print(my_tree.root.right.value)
print(my_tree.root.left.value)




def see(value):
    if my_tree.contains(value):
        print('El valor existe: ',value)
    else:
        print('Nada que ver')


see(33)