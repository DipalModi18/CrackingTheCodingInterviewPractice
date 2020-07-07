# Reference: https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/2382/


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


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(None)
        my_list = l3

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                my_list.next = ListNode(l1.val)
                l1 = l1.next
            else:
                my_list.next = ListNode(l2.val)
                l2 = l2.next
            my_list = my_list.next
        my_list.next = l1 or l2
        return l3.next


if __name__ == "__main__":
    l1_elements = [1, 2, 4]
    l2_elements = [1, 3, 4]
    l1 = createList(l1_elements)
    l2 = createList(l2_elements)
    print("l1: {}".format(printList(l1)))
    print("l2: {}".format(printList(l2)))
    head = Solution().mergeTwoLists(l1=l1, l2=l2)
    print("l: {}".format(printList(head)))
