
#Create class for indivual node in the list
class Listnode:
    def __init__(self,data):
        self.data=data
        self.next=None

    def __str__(self):
        return str(self.data)
    
class Linkedlist:
    def __init__(self):
        self.head=None

    def insert(self,value):
        new_node=Listnode(value)
        new_node.next=self.head
        self.head=new_node

    def display(self):
        iterator=self.head
        while iterator is not None:
            print(iterator , end=" ")
            iterator=iterator.next

    def find(self,value):
        iterator=self.head
        while iterator is not None:
            if iterator.data==value:
                return iterator
            iterator=iterator.next
        return None
    
    def remove(self,value):
        iterator=self.head
        prev_it=None
        while iterator is not None:
            if iterator.data==value:
                if prev_it is None:
                    self.head=iterator.next
                else:
                    prev_it.next=iterator.next
                return True
            prev_it=iterator
            iterator=iterator.next
        return False



data=Linkedlist()
data.insert("Pakistan")
data.insert("Greece")
data.insert("Italy")
data.insert("Sweden")
data.insert("Dubai")
data.display()

print()

it=data.find("Italy")
print(f'Looking for Italy and found {it}')
it=data.find("Qatar")
print(f'Looking for Qatar and found {it}')

data.remove("Italy")
data.remove("Greece")
data.display()

    






    