# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree(object):
    bstArr = []

    def __init__(self, bstArr):
        super()
        self.bstArr = bstArr

    def constructBST(self, root, i):
        """
        Construct BST using recursion
        :param root:
        :param i:
        :return:
        """
        leftIndex = 2 * i + 1  # left Index is the value of the left child, index refers to the position in the bstArr
        rightIndex = 2 * i + 2
        if leftIndex < len(self.bstArr):
            left = TreeNode(val=self.bstArr[leftIndex], left=None, right=None)
            root.left = left
            self.constructBST(root.left, leftIndex)
        if rightIndex < len(self.bstArr):
            right = TreeNode(val=self.bstArr[rightIndex], left=None, right=None)
            root.right = right
            self.constructBST(root.right, rightIndex)

    def printBST(self, root):
        if root is not None:
            print("root: {} || left: {} || right: {}".format(
                root.val,
                root.left.val if root.left is not None else None,
                root.right.val if root.right is not None else None
            ))
            self.printBST(root.left)
            self.printBST(root.right)