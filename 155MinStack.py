class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []

        

    def push(self, val):
        self.stack.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            if val < self.minStack[-1]:
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[-1])
        

    def pop(self):
        self.stack.pop()
        self.minStack.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.minStack[-1]
    

if __name__ == "__main__":
    s = MinStack()
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(1)

    print(s.getMin())
    print(s.pop())
    print(s.getMin())

