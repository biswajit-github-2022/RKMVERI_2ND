from Stack_using_array import ArrayStack 
from postfix import evaluate_postfix


def evaluate_prefix(exprsn):
    reverse_expression= exprsn[::-1]
    value=evaluate_postfix(reverse_expression)
    return value

f=1
while f:
    exprsn = input("Enter the prefix expression : ")
    print(evaluate_prefix(exprsn))
    f= int(input("f: "))




#   +1%/*/*23+4567^89
    
# Enter the prefix expression : /*23+45
# 1.5
# f: 1       
# Enter the prefix expression : */*23+456
# 9.0
# f: 1
# Enter the prefix expression : /*/*23+4567
# 0.7777777777777778
# f: 1
# Enter the prefix expression : %/*/*23+4567^89
# 0.11111111042837596
# f: 1
# Enter the prefix expression : +1%/*/*23+4567^89
# 1.111111110428376
# f: 0