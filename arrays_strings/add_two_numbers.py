from linked_list import ListNode, createList, printList
# Reference: https://leetcode.com/problems/add-two-numbers/


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        l = head
        rem = 0
        prevRem = 0
        while l1 is not None:
            val = (l1.val + l2.val) % 10
            l.next = ListNode(val + prevRem)
            prevRem = int(((l1.val + l2.val) - val)/10)
            l = l.next
            l1 = l1.next
            l2 = l2.next
        return head.next


if __name__ == "__main__":
    l1 = createList([3, 4, 3])
    l2 = createList([5, 6, 4])
    print("l1: {}".format(printList(l1)))
    print("l2: {}".format(printList(l2)))
    l = Solution().addTwoNumbers(l1=l1, l2=l2)
    print("l: {}".format(printList(l)))
