class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        subsets = []
        self.get_all_subsets(nums, 0, [], subsets)
        return subsets
        
    @staticmethod
    def get_all_subsets(nums, idx, current_subset, subsets):
        subsets.append(list(current_subset))
        while idx < len(nums):
            current_subset.append(nums[idx])
            Solution.get_all_subsets(nums, idx + 1, current_subset, subsets)
            current_subset.pop()
            idx += 1
        