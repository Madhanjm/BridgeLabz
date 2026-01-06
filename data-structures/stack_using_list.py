class stack:
    def __init__(self):
        self.stack=[]
        
    def push(self,element):
        self.stack.append(element)
        
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack)==0
    
    def size(self):
        return len(self.stack)
    
s=stack()
s.push("A")
s.push("B")
print(stack)
print(s.pop())

print(s.isEmpty())

print(s.size())