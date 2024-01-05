array=[5, 6, 7, 9, 10, 12]

def binary_search(x,key):
    l=0;r=len(x)-1
    while l<=r:
        mid=int((r+l)/2)
        if x[mid]==key:
            return 1 
        if key<x[mid]:
            r=mid-1
        if x[mid]<key:
            l=mid+1
    return 0

print(binary_search(array,6))
