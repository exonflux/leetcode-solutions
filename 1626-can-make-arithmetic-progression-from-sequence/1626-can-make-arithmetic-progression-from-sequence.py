class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        diff = arr[1] - arr[0]
        return all(arr[i] - arr[i - 1] == diff for i in range(2, len(arr)))
        