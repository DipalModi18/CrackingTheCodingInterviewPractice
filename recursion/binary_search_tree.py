# Reference: https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/3233/

bstArr = [4, 2, 7, 1, 3]


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        elif root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)


def constructBST(root, i):
    """
    Construct BST using recursion
    :param root:
    :param i:
    :return:
    """
    leftIndex = 2 * i + 1  # left Index is the value of the left child, index refers to the position in the bstArr
    rightIndex = 2 * i + 2
    if leftIndex < len(bstArr):
        left = TreeNode(val=bstArr[leftIndex], left=None, right=None)
        root.left = left
        constructBST(root.left, leftIndex)
    if rightIndex < len(bstArr):
        right = TreeNode(val=bstArr[rightIndex], left=None, right=None)
        root.right = right
        constructBST(root.right, rightIndex)


def printBST(root):
    if root is not None:
        print("root: {} || left: {} || right: {}".format(
            root.val,
            root.left.val if root.left is not None else None,
            root.right.val if root.right is not None else None
        ))
        printBST(root.left)
        printBST(root.right)


if __name__ == "__main__":
    root = TreeNode(val=bstArr[0], left=None, right=None)
    constructBST(root, 0)
    print("BST Constructed")
    printBST(root)

    node = Solution().searchBST(root=root, val=7)
    if node is not None:
        print("Found TreeNode: {}".format(node.val))
    else:
        print("Node not found")
