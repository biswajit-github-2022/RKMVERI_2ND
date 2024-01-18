arr=[1,2,3,4,5,6]
first=0
last=len(arr)-1
def reverse_arr(x,f,l):
    if f>l:
        return x
    x[f],x[l] = x[l],x[f]
    return reverse_arr(x,f+1,l-1)
print(reverse_arr(arr,first,last))