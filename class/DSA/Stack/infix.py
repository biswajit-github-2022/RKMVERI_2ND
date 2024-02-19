from  Stack_using_array import ArrayStack
operands = ArrayStack()
operators = ArrayStack()
def evaluate(operand1,operator,operand2):
    if operator == '+':
        operands.push(operand2 + operand1)
    elif operator == '-':
        operands.push(operand2 - operand1)
    elif operator == '*':
        operands.push(operand2 * operand1)
    elif operator == '/':
        operands.push( operand2 / operand1)
    elif operator == '^':
        operands.push( operand2 ** operand1)
    elif operator == '%':
        operands.push( operand2 % operand1)
def evaluate_infix(expression):
    
    for char in expression:
        if char == ' ':
            continue
        elif char.isdigit():
            operands.push(int(char))
        elif char == '(':
            continue
        elif char == '+' or char == '-' or char == '*' or char == '/' or char == '^' or char == '%':
            operators.push(char)
        elif char == ')':
            operator = operators.pop()
            operand1=operands.pop()
            operand2=operands.pop()
            evaluate(operand1,operator,operand2)
    return operands.pop()

f=1
while f:
    infix_expression = input("Enter the infix expression : ")
    result = evaluate_infix(infix_expression)
    print(result) 
    #  (1+(((((2*3)/(4+5))*6)/7)%(8^9)))
    f=int(input("f: "))


# output
# Enter the infix expression : (2*3)
# 6
# f: 1
# Enter the infix expression : (2*3)/(4+5)
# 9
# f: 1
# Enter the infix expression : ((2*3)/(4+5))
# 0.6666666666666666
# f: 1
# Enter the infix expression : (1+(1+(((((2*3)/(4+5))*6)/7)%(8^9)))
# 1.5714285714285714