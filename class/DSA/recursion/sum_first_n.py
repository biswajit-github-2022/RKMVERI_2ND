def sum(a,n):
    if n==0 :
        return 0
    return a[n-1]+sum(a,n-1)

print(sum([1,2,3,4,5,6,7,8,9,10],5))