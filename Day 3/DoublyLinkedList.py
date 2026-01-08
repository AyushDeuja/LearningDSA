class Node:
    def __init__(self, value = None):
        self.data = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, head = None):
        self.head = head

    def insertAtEnd(self, value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        t = self.head
        while(t.next != None):
            t = t.next
        t.next = temp
        temp.prev = t

    def insertAtBeginning(self, value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp        
        self.head = temp

    def printList(self):
        t1 = self.head
        while(t1 != None):
            print(t1.data, end = "<--> ")
            t1 = t1.next

obj = DoublyLinkedList()
obj.insertAtEnd(10) 
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBeginning(5)
obj.printList()