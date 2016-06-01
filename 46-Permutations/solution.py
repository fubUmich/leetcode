class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        final_perms = []
        self.next_permutation(nums, set(), [], final_perms)
        return final_perms
        
    @staticmethod
    def next_permutation(nums, used_nums, current_perm, final_perms):
        if len(current_perm) == len(nums):
            final_perms.append(list(current_perm))
            return
        
        for next_num in nums:
            if next_num not in used_nums:
                current_perm.append(next_num)
                used_nums.add(next_num)
                Solution.next_permutation(nums, used_nums, current_perm, final_perms)
                current_perm.pop()
                used_nums.remove(next_num)