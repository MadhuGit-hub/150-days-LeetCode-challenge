class Solution(object):
    def removeDuplicates(self, nums):
        unique = set()
        for i in nums:
            if i not in unique:
                unique.add(i)
        nums[:]=unique
        nums.sort()
        return len(nums)
