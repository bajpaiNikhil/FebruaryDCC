class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def intersectionInList(listA, listB):
    if listA is None or listB is None:
        return None
    a = listA
    b = listB
    while a is not b:
        a = listB if a is None else a.next
        b = listA if b is None else b.next
    return a

listA = Node(4)
listA.next = Node(1)
listA.next.next = Node(8)
listA.next.next.next = Node(4)
listA.next.next.next.next = Node(5)

listB = Node(5)
listB.next = Node(6)
listB.next.next = Node(1)
listB.next.next.next = Node(8)
listB.next.next.next.next = Node(4)

print(intersectionInList(listA, listB))
