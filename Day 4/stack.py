class Stack:
    def __init__(self):
        self.s = []

    def length(self):
        return len(self.s)
    
    def push(self, value):
        self.s.append(value)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.s.pop()