from Queue_using_array import ArrayQueue

def reverse(queue:ArrayQueue):
    if queue.is_empty(): 
        return
    e=queue.dequeue()
    reverse(queue)
    queue.enqueue(e)
    # while not queue.is_empty():
    #     e=queue.dequeue()
    #     print(e)
    #     reverse(queue)
    #     queue.enqueue(e)
    # return queue

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

print(queue)

reverse(queue)

print(queue)