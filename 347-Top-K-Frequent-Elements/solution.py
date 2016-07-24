class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        bucket = [None] * (len(nums) + 1)
        for (num, freq) in frequency.items():
            if bucket[freq] == None:
                bucket[freq] = []
            bucket[freq].append(num)
        
        result = []
        for i in reversed(range(len(nums) + 1)):
            if k > 0:
                if bucket[i] is not None:
                    result.extend(bucket[i])
                    k -= len(bucket[i])
            else:
                break
            
        return result
        