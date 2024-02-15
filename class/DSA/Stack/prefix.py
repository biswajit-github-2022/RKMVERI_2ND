from Stack_using_array import ArrayStack 

def evaluate(op1,oprator,op2):
    op1=float(op1)
    op2=float(op2)
    if oprator=="+":
        return(op1+op2)
    elif oprator=="-":
        return(op1-op2)
    elif oprator=="*":
        return(op1*op2)
    elif oprator=="/":
        return(op1/op2)
    elif oprator=="^":
        return(op1**op2)
    elif oprator=="%":
        return(op1%op2)

def evaluate_prefix(exprsn):
    stack=ArrayStack()
    for char in exprsn:
        if char.isdigit():
            if type(stack.top()) == int or float:
                op1=stack.pop()
                if type(stack.top()) == int or float:
                    op2=stack.pop()
                    oprator=stack.pop()
                    op1=evaluate(op2,oprator,op1)
                op2=int(char)
                oprator=stack.pop()
                stack.push(evaluate(op1,oprator,op2))
            else:
                stack.push(int(char))
        else:
            if char.isdigit():
                stack.push(int(char))
                continue
            stack.push(char)
    if stack.__len__()>1:
        for i in range(stack.__len__()-1):
            op2=stack.pop()
            op1=stack.pop()
            oprator=stack.pop()
            stack.push(evaluate(op1,oprator,op2))
            if stack.__len__()==1:
                return stack.pop()
    return stack.pop()

exprsn = input("Enter the prefix expression : ")
print(evaluate_prefix(exprsn))