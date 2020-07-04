# Reference: https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/3233/
from binary_search_tree import TreeNode, BinarySearchTree


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


if __name__ == "__main__":
    bstArr = [4, 2, 7, 1, 3]
    bst = BinarySearchTree(bstArr=bstArr)
    root = TreeNode(val=bst.bstArr[0], left=None, right=None)
    bst.constructBST(root, 0)
    print("BST Constructed")
    bst.printBST(root)

    node = Solution().searchBST(root=root, val=7)
    if node is not None:
        print("Found TreeNode: {}".format(node.val))
    else:
        print("Node not found")
