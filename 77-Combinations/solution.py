class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        nums = [i for i in xrange(1, n+1)]
        result = []
        self.find_combines(nums, result, 0, [], k)
        return result
        
    def find_combines(self, nums, result, idx, current_comb, k):
        if len(current_comb) == k:
            result.append(list(current_comb))
            return
        
        for i in range(idx, len(nums)):
            current_comb.append(nums[i])
            self.find_combines(nums, result, i+1, current_comb, k)
            current_comb.pop()