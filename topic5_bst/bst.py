
class TreeNode:
    def __init__(self,value):
        self.value=value
        self.parent=None
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def is_empty(self):
        return self.root is None

   