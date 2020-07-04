# Reference: https://leetcode.com/explore/learn/card/recursion-i/256/complexity-analysis/2375/


# Definition for a binary tree node.
from binary_search_tree import TreeNode, BinarySearchTree


class Solution(object):

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == "__main__":
    bstArr = [3, 9, 20, None, None, 15, 7]
    bst = BinarySearchTree(bstArr=bstArr)
    root = TreeNode(val=bst.bstArr[0], left=None, right=None)
    bst.constructBST(root, 0)
    print("BST Constructed")
    bst.printBST(root)

    print("Max Depth: {}".format(Solution().maxDepth(root)))
