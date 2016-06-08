# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.generate_trees_with_nums([i for i in range(1, n+1)])
        
    def generate_trees_with_nums(self, nums):
        if len(nums) == 0:
            return [None]
        elif len(nums) == 1:
            return [TreeNode(nums[0])]
        else:
            result_list = []
            for i in range(len(nums)):
                left_nodes = self.generate_trees_with_nums(nums[:i])
                right_nodes = self.generate_trees_with_nums(nums[i+1:])
                for left_node in left_nodes:
                    for right_node in right_nodes:
                        result_list.append(TreeNode(nums[i]))
                        result_list[-1].left = left_node
                        result_list[-1].right = right_node
            return result_list
                