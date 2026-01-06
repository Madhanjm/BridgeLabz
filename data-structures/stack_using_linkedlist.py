class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self):
        self.head=None
        self.size=0
        
    def push(self,value):
        new_node=Node(value)
        if self.head:
            new_node.next=self.head
        self.head=new_node
        self.size+=1
        
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        pop_element=self.head
        self.head=self.head.next
        self.size-=1
        return pop_element.value
    
    def peek(self):
        if self.isEmpty():
            return "stack is empty "
        return self.head.value
    
    def isEmpty(self):
        return self.size==0
    
    def stack_size(self):
        return self.size
    
    def traversal(self):
        current_node=self.head
        while current_node:
            print(current_node.value,end=" ")
            current_node=current_node.next
        print()
        
        
my_stack=Stack()
my_stack.push(1)
my_stack.push(2)

my_stack.traversal()

print(my_stack.peek())

print(my_stack.pop())

print(my_stack.isEmpty())

print(my_stack.stack_size())




            
        