class Solution(object):
    def removeElement(self, nums, val):
        temp = []
        for i in nums:
            if val != i:
                temp.append(i)
                
        nums[:]=temp
        return len(nums)
        