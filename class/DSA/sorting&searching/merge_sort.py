def sort(arr,L,R):
    i=j=k=0
    while i<len(L) and j<len(R):
        if L[i]<=R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
    while i<len(L):
        arr[k]=L[i]
        i+=1
        k+=1
    while j<len(R):
        arr[k]=R[j]
        j+=1
        k+=1
def merge(arr):
    if len(arr)>1:
        mid= len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        merge(L)
        merge(R)
        sort(arr,L,R)
        return arr
x=[32,4,45,3,4,6,73,346,7,552,34]
print(merge(x))