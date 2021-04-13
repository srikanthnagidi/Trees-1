"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Input: root = [2,1,3]
Output: true


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4    

"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
    
class Solution:

    def __init__(self, isBst = True, prev=None, node=None):
        self.isBst = isBst
        self.prev = prev
        self.node = node

    # given the list of numbers build tree
    # children of ith elements are 2*i + 1 and 2*i + 2

    def buildTree(self, nums:List):
        self.node =  self.insertRecurrsion(self.node, nums, 0)
        return self.node

    def insertRecurrsion(self, node, nums, i):
        if(i < len(nums) and nums[i] != None):
            temp = TreeNode(nums[i])
            node = temp
            node.left = self.insertRecurrsion(temp.left, nums, 2*i+1)
            node.right = self.insertRecurrsion(temp.right, nums, 2*i+2)
        
        return node
    
    def printBstInOrder(self, node):
        if(node == None):
            return
        self.printBstInOrder(node.left)
        print(node.val, end=",")
        self.printBstInOrder(node.right)

    def isValidBst(self, root: TreeNode):
        if (root == None):
            return True

        self.inOrder(root)
        return self.isBst

    def inOrder(self, root:TreeNode):
        if(root == None):
            return
        
        self.inOrder(root.left)
        if(self.prev != None and self.prev.val >= root.val):
            self.isBst = False
        self.prev = root
        self.inOrder(root.right)

sol = Solution()
print(sol.isValidBst(sol.buildTree([2,1,3])))
print(sol.isValidBst(sol.buildTree([5,1,4,None,None,3,6])))