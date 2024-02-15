from Stack_using_array import ArrayStack 

stack1=ArrayStack()
stack2=ArrayStack()
stack3=ArrayStack()
print("Stack 1: ")
for i in range(6):
    stack1.push(i)
    print(stack1.top())

def reverse_stack(stack1,stack2,stack3):
    while stack1.__len__()!=1:
        stack2.push(stack1.pop())
    stack3.push(stack1.pop())

    while stack2.__len__()!=1:
        stack3.push(stack2.pop())
    stack1.push(stack2.pop())

    while stack3.__len__()!=0:
        stack1.push(stack3.pop())
        
    return stack1

print(reverse_stack(stack1,stack2,stack3))
