class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i, j in enumerate(nums):
            r = target - j
            if r in d: return [d[r], i]
            d[j] = i