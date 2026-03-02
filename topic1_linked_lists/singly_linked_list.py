
class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None

    def __str__(self):
        return str(self.data)
    

class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,value):
        new_node= ListNode(value)
        new_node.next=self.head
        self.head=new_node

    def display(self):
        iterator= self.head
        while iterator is not None:
            print(iterator)
            iterator=iterator.next

    def find(self,value):
        iterator=self.head
        while iterator is not None:
            if iterator.data== value:
                return iterator
            iterator = iterator.next
        return None
    
    def remove(self,value):
        iterator= self.head
        prev_iterator=None
        while iterator is not None:
            if iterator.data==value:
                if prev_iterator is None: # first node to be deleted
                    self.head=iterator.next
                else:
                    prev_iterator.next=iterator.next
                return True
            prev_iterator=iterator
            iterator =iterator.next
        return False


data = LinkedList()
data.insert(18)
data.insert(20)
data.insert(16)
data.insert(5)
data.display()


it= data.find(16)
print(f'Looking for 16 and got {it}')
it =data.find(30)
print(f'Looking for 30 and got {it}')

data.remove(20)
data.remove(18)
data.remove(5)
data.display()