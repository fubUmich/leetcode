class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quickSelect(nums, 0, len(nums) -1, k)
        
    def quickSelect(self, array, low, high, k):
        i = low
        j = high - 1
        pivot = array[high]
        
        while i <= j:
            if array[i] > pivot:
                array[i], array[j] = array[j], array[i]
                j -= 1
            else:
                i += 1
            
        array[i], array[high] = array[high], array[i]
        
        """
              j i
              | |
              V V        
        1 3 2 4 6 9 12 7
        ^       ^      ^
        |       |      |
       low    pivot   high
       
        So there are high - i numbers larger than pivot.
        """
        
        if high - i == k - 1:
            return pivot
        elif high - i < k - 1:
            return self.quickSelect(array, low, i-1, k - (high - i + 1))
        else:
            return self.quickSelect(array, i, high, k)
        
        