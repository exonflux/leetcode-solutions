class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=2

        n = len(nums)
        
        for i in range(2,n):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k+=1

        return k
                