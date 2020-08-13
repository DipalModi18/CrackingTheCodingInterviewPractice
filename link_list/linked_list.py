# Problem: https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if self.head is None:
            return -1
        i = 0
        cur = self.head
        while i != index and cur.next is not None:
            cur = cur.next
            i = i + 1
        if i == index:
            return cur.val
        return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        if self.head is None:
            self.head = Node(val)
        else:
            cur = Node(val)
            cur.next = self.head
            self.head = cur

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == 0:
            self.addAtHead(val)
        i = 0
        cur = self.head
        index = index - 1
        while i != index and cur.next is not None:
            cur = cur.next
            i = i + 1
        if i == index:
            new_node = Node(val)
            new_node.next = cur.next
            cur.next = new_node

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index == 0:
            self.head = self.head.next
            return
        i = 0
        cur = self.head
        index = index - 1
        while i != index and cur.next is not None:
            cur = cur.next
            i = i + 1
        if i == index:
            delete_node = cur.next
            if delete_node is not None:
                cur.next = delete_node.next

    def print_list(self):
        cur = self.head
        i = 0
        while cur is not None:
            print("[{}]: {}".format(i, cur.val))
            cur = cur.next
            i = i + 1


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
param_1 = obj.get(0)
print(param_1)
obj.addAtHead(1)
obj.print_list()
obj.deleteAtIndex(0)
obj.print_list()
