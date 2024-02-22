class ArrayQueue:
    DEFAULT_CAPACITY=10
    
    def __init__(self):
        self._data=[None]*ArrayQueue.DEFAULT_CAPACITY
        self._size=0
        self._front=0
    
    def __len__(self):
        return self.size

    def is_empty(self):
        if self._size == 0:
            return True
        return False
    
    def first(self):
        if self.is_empty():
            raise Exception ("Queue is empty")
        return self._data[self._front]
    def last(self):
        if self.is_empty():
            raise Exception ("Queue is empty")
        return self._data[self._front+self._size-1]
    
    def dequeue(self):
        '''
        delete_first
        '''
        if self.is_empty():
            raise Exception ("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front]= None
        self._front= (self._front+1) % len(self._data)
        self._size-=1
        return answer
    def delete_last(self):
        if self.is_empty():
            raise Exception ("Queue is empty")
        rare=self._front+self._size-1
        answer=self._data[rare]
        self._data[rare]= None
        rare=(rare-1)%len(self._data)
        self._size-=1
        return answer
    def add_first(self,e):
        if self.is_full():
            self._resize(2*len(self._data))
        avail= (self._front-1)% len(self._data)
        self._data[avail]=e
        self._size+=1
    def enqueue(self,e):
        '''
        add_last
        '''
        if self._size==len(self._data):
            self._resize(2*len(self._data))
        avail= (self._front+self._size)% len(self._data)
        self._data[avail]=e
        self._size+=1

    def resize(self,cap):
        old =self._data
        self.data=[None]*cap
        walk= self._front
        for k in range(self._size):
            self._data[k]=old[walk]
            walk= (1+walk)%len(old)
        self._front=0
    def __str__(self):
        return str(self._data)

queue=ArrayQueue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)
queue.enqueue(70)
queue.enqueue(80)
queue.enqueue(90)
queue.enqueue(100)

print(queue.first())
print(queue.last())

queue.dequeue()
queue.delete_last()

print(queue.first())
print(queue.last())