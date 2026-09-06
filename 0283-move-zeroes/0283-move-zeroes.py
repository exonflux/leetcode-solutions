class Solution(object):
    def moveZeroes(self, nums):

        position = 0

        for i in range (len(nums)):
            if nums[i] != 0:
                nums[position] = nums[i]
                position += 1

        for i in range (position,len(nums)):
            nums[i] = 0


        return nums