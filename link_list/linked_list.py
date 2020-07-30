# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def createList(elements):
    l = ListNode(elements[0])
    head = l
    for i in range(1, len(elements)):
        tmp = ListNode(elements[i])
        l.next = tmp
        l = l.next
    return head


def printList(head):
    l = []
    while head is not None:
        l.append(head.val)
        head = head.next
    return l
