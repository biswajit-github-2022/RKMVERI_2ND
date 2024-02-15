class ArrayStack:
    def __init__(self):
        self._data=[]
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data)==0
    def push(self,e):
        self._data.append(e)
    def top(self):
        if self.is_empty():
            # return None
            raise Exception("Stack is Empty")
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            # return None
            raise Exception("Stack is Empty")
        return self._data.pop()
    
# stack =ArrayStack()
# stack.push(1)
# stack.push(2)


# print(stack.top())#10

# stack.pop() 
# stack.pop()

# print(stack.top()) #8

# print(stack.is_empty()) #False

# print(stack.__len__()) #8