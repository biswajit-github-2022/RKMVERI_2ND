class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_middle(head):
    if not head:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
# i=0
# while i<=5:
#     head=ListNode(i)
#     head=head.next
#     i+=1

middle = find_middle(head)
if middle:
    print("Middle element is:", middle.val)
else:
    print("Linked list is empty.")