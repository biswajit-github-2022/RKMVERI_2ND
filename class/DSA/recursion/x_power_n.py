# O(n) algorithm
# def pow(x,n):
    # if n==0:
        # return 1
    # if n==1:
        # return x
    # return x*pow(x,n-1)

# O(logn) algorithm
def pow(x,n):
    if n==0:
        return 1
    else:
        accumulate=pow(x,n//2)
        result=accumulate*accumulate
        if n%2!=0:
            result*=x
    return result
print(pow(2,4))