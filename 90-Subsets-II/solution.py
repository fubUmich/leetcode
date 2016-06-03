class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        all_subsets = []
        self.get_all_subsets(sorted(nums), 0, [], all_subsets)
        return all_subsets
        
    def get_all_subsets(self, nums, start, current_subset, all_subsets):
        all_subsets.append(current_subset)
        for i in xrange(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            self.get_all_subsets(nums, i + 1, current_subset + [nums[i]], all_subsets)
            