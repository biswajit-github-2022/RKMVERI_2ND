x=[3,2,4,3,1,5,4,5,9,6]
def bubble_sort(x):
    for i in range(len(x)):
        for j in range(0,len(x)-i-1):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
bubble_sort(x)
print(x)