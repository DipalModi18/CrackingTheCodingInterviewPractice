from linked_list import ListNode, createList, printList
# Reference: https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/2382/
# TODO: Incomplete for some test cases


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
    l1 = createList(elements=[1, 2, 4])
    l2 = createList(elements=[1, 3, 4])
    print("l1: {}".format(printList(l1)))
    print("l2: {}".format(printList(l2)))
    head = Solution().mergeTwoLists(l1=l1, l2=l2)
    print("l: {}".format(printList(head)))
