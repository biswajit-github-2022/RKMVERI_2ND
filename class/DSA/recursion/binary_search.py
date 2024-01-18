def binary_search(a,k,l,h):
    if l>h:
        return f'cannot find {k}'
    mid=(l+h)//2
    if a[mid]==k:
        return f'found {k} at index {mid}'
    elif a[mid]<k:
        return binary_search(a,k,mid+1,h)
    else:
        return binary_search(a,k,l,mid-1)

arr=[1,2,3,4,5,6,7,8]
key=4
low=0
high=len(arr)-1
print(binary_search(arr,key,low,high))