class Dequeue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def InsertionAtEnd(self, item):
        self.items.append(item)

    def DeleteAtFront(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("dequeue from empty queue")

    def InsertionAtFront(self, item):
        self.items.insert(0, item)

    def DeleteAtEnd(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("dequeue from empty queue")
    
dequeue = Dequeue()
dequeue.InsertionAtEnd(10)
dequeue.InsertionAtEnd(20)
dequeue.InsertionAtFront(5)
dequeue.InsertionAtFront(30)
print(dequeue.DeleteAtFront())  # Output: 5
print(dequeue.DeleteAtEnd())    # Output: 20
print(dequeue.DeleteAtFront())  # Output: 10
print(dequeue.DeleteAtEnd())    # Output: 30

