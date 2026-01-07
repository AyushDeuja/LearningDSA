class Node:
    def __init__(self, info, next = None):
        self.data = info
        self.next = next

class SignlyLinkedList:
    def __init__(self, head = None):
        self.head = head

    def insertAtEnd(self, value):
        temp = Node(value)
        if(self.head != None):
            t1 = self.head 
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def insertAtBeginning(self, value):
        temp = Node(value)
        if(self.head != None):
            temp.next = self.head
        self.head = temp

    def insertAtMiddle(self,  value, x):
        temp = Node(value)
        t1 = self.head
        while(t1.next != None):
            if(t1.data == x):
                temp.next = t1.next
                t1.next = temp
                break
            t1 = t1.next

    def deleteList(self, value):

        t1 = self.head
        prev = t1
        if(t1.data == value):
            self.head = t1.next
            return
        while(t1 != None):
            if(t1.data == value):
                prev.next = t1.next
                break
            else:
                prev = t1
                t1 = t1.next 
        if(t1.data == None):
            prev.next = None

    def printList(self):
        t1 = self.head
        while(t1 != None):
            print(t1.data, end = " ")
            t1 = t1.next

obj = SignlyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBeginning(5)
obj.insertAtMiddle(15, 10)
obj.deleteList(30)
obj.printList()