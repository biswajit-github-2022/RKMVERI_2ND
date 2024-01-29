def max_recursion(arr):
    if len(arr)==1:
        return arr[0]
    else:
        return max(arr[0],max_recursion(arr[1:]))

x=[1,2,3,4,4,56,6]
print(max_recursion(x))