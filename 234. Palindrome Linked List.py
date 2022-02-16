class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def palindromeList(head):
    fast = slow = cur = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    stack = [slow.val]

    while slow.next:
        slow = slow.next
        stack.append(slow.val)

    while stack:
        if stack.pop() != cur.val:
            return False
        cur = cur.next
    return True


head = Node(1)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(1)

print(palindromeList(head))
