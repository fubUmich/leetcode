class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        self.get_all_subsets(sorted(nums), 0, [], subsets)
        return subsets
        
    @staticmethod
    def get_all_subsets(nums, start, current_subset, subsets):
        subsets.append(current_subset)
        for i in xrange (start, len(nums)):
            Solution.get_all_subsets(nums, i + 1, current_subset + [nums[i]], subsets)