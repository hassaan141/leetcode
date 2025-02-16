#uses a node class to create a linked list 

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        traverse = self.head

        if self.head == None:
          self.head = new_node
          return
          
        while traverse.next != None:
            traverse = traverse.next 
        traverse.next = new_node
    
    def printList(self):
        traverse = self.head
        result = []

        if traverse == None:
            print("List is empty")
            return

        while traverse != None:
          result.append(traverse.data)
          traverse = traverse.next
        print(result)

    def get(self, index):
        traverse = self.head
        count = 0

        while count != index:
            traverse = traverse.next
            count += 1
        
        print(traverse.data)
    
    def delete(self, index):
        traverse = self.head
        count = 0

        while count!=index-1:
            traverse = traverse.next
            count +=1
        
        traverse.next = traverse.next.next





list1 = LinkedList()
list1.printList()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.printList()
list1.get(1)
list1.delete(1)
list1.printList()


