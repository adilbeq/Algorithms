class Stack:
    def __init__(self):
        self.arr = []
        self.size = 0
    def push(self, element):
        self.arr.append(element)
        self.size += 1
    def pop(self):
        el = self.arr[self.size - 1]
        self.arr.pop()
        self.size -= 1
        return el
    def top(self):
        return self.arr[self.size - 1]
    def sizeOfStack(self):
        return self.size

brackets = input() # ())((())
s = Stack()
mx = 0
s.push(-1)
for i in range(len(brackets)):
    if brackets[i] == '(':
        s.push(i)
    else:
        s.pop()
        if s.sizeOfStack() == 0:
            s.push(i)
        else:
            mx = max(mx, i-s.top())
print(mx)
