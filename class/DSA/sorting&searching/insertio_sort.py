array=[6,7,5,10,9,12]
def insertion_sort(x):
    for i in range(1,len(x)):
        key=x[i]
        j=i-1
        while(x[j]>key and j>=0):
            x[j+1]=x[j]
            j=j-1
        x[j+1]=key
    return x
print(insertion_sort(array))