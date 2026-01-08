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

    def insertAtMiddle(self, value, x):
        t = self.head
        while(t.next != None):
            if(t.data == x):
                break
            else:
                t = t.next
        temp = Node(value)
        t.next.prev = temp
        temp.next = t.next
        t.next = temp
        temp.prev = t


    def printList(self):
        t1 = self.head
        while(t1 != None):
            print(t1.data, end = "<--> ")
            t1 = t1.next

    def deleteList(self, value):
        if(self.head == None):
            print("List is empty")
            return
        t = self.head
        if(t.data == value):
            self.head = t.next
            self.head.prev = None 
            return
        while(t.next != None):
            if(t.data == value):
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            else:
                t = t.next
        if(t.data == value):
            t.prev.next = None
                
        

obj = DoublyLinkedList()
obj.insertAtEnd(10) 
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBeginning(5)
obj.insertAtMiddle(15, 10)
obj.deleteList(15)
obj.deleteList(30)
obj.printList()