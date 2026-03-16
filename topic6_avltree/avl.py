
class TreeNode:
    def __init__(self, value):
        self.value = value 
        self.parent = None 
        self.left = None 
        self.right = None 
        self.height = 1

    def __str__(self):
        return f"{str(self.value)}, h={self.height}"
    

class AVLTree:
    def __init__(self):
        self.root = None 

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def update_height(self, node): 
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def find_successor(self, node):
        right = node.right
        while right.left:
            right = right.left
        return right


    def insert_value(self, value):
        self.root = self.insert_node(self.root, value, None)

    
    def insert_node(self, node, value, parent):
        if node is None:
            new_node = TreeNode(value)
            new_node.parent = parent 
            return new_node
        
        if value < node.value:
            node.left = self.insert_node(node.left, value, node)
        elif value > node.value:
            node.right = self.insert_node(node.right, value, node)
        else:
            return node
        
        self.update_height(node)
        # Rebalance if necessary
        return node
        

    def delete_value(self, value):
        self.root = self.delete_node(self.root, value)

    def delete_node(self, node, value):
        if node is None:
            return None 
        
        if value < node.value:
            node.left = self.delete_node(node.left, value)
            if node.left is not None:
                node.left.parent = node 
        elif value > node.value:
            node.right = self.delete_node(node.right, value)
            if node.right is not None:
                node.right.parent = node 
        else:   # Node to be deleted is found
            if node.left is None: 
                replace = node.right
                if replace is not None:
                    replace.parent = node.parent
                return replace
            elif node.right is None:
                replace = node.left
                if replace is not None:
                    replace.parent = node.parent
                return replace
            
            successor = self.find_successor(node)
            node.value = successor.value
            node.right = self.delete_node(node.right, successor.value)
            if node.right is not None:
                node.right.parent = node

        self.update_height(node)

        # Rebalance if necessary
        return node
    


    def display(self):
        if self.root is None:
            print("Tree is empty")
            return
        self.inorder(self.root)

    def inorder(self, node):
        if node.left is not None:
            self.inorder(node.left) 
        print(node)
        if node.right is not None:
            self.inorder(node.right)



# data = [100, 45, 140, 11, 35, 68, 110, 200]
data = [10, 20, 30, 40, 50, 60, 70, 80]
tree = AVLTree()
for value in data:
    tree.insert_value(value)
tree.display()

# print("Delete ")
# tree.delete_value(11)
# tree.delete_value(68)
# tree.delete_value(140)
# tree.display()

        



