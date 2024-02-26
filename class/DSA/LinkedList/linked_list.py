class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

# x=[1,2,3,4]
# ll=LinkedList()
# for i in range(len(x)):
#     if i==0:
#         ll.head = Node(x[i])
#         ll.tail = ll.head
#     else:
#         ll.tail.next = Node(x[i])
#         ll.tail = ll.tail.next

# for i in ll.__iter__():
#     print(i.data,"\n")