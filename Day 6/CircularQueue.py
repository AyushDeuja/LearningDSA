class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.front = -1
        self.rear = -1

    def Enqueue(self, item):
        if (self.rear + 1) % self.front:
            raise OverflowError("Queue is full")
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.items[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = item

    def Dequeue(self):
        if self.front == -1:
            raise IndexError("Queue is empty")
        elif self.front == self.rear:
            item = self.items[self.front]
            self.front = -1
            self.rear = -1
            return item
        else:
            item = self.items[self.front]
            self.front = (self.front + 1) % self.size
            return item