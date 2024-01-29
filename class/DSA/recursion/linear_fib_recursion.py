def fibonacci(n):
    return fibo_helper(n,1,0)

def fibo_helper(n,a,b):
    # if n==0:
    #     return b
    if n==1 :
        return a
    return fibo_helper(n-1,a+b,a)

print(fibonacci(10))