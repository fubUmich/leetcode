class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        subsets = [[]]
        for num in nums:
            subsets += [subset + [num] for subset in subsets]
            
        return subsets
        
