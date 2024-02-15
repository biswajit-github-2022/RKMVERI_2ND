from Stack_using_array import ArrayStack 

def evaluate_postfix(exprsn):
    stack=ArrayStack()
    for char in exprsn:
        if char.isdigit():
            stack.push(int(char))
        else:
            op2=stack.pop()
            op1=stack.pop()
            if char=="+":
                stack.push(op1+op2)
            elif char=="-":
                stack.push(op1-op2)
            elif char=="*":
                stack.push(op1*op2)
            elif char=="/":
                if op2==0:
                    raise Exception("Invalid expression : Cannot divide by 0")
                stack.push(op1/op2)
            elif char=="^":
                stack.push(op1**op2)
            elif char=="%":
                stack.push(op1%op2)
    if stack.__len__()!=1: raise Exception("Invalid expression")
    return stack.pop()

exprsn = input("Enter the postfix expression : ")
print(evaluate_postfix(exprsn))