class Solution(object):
    def rotate(self, nums, k):
        k = k%len(nums)
        arr = []
        arr2 =[]
        arr = nums[-k:]
        arr2 = nums[:-k]
        nums[:] = arr+arr2
        
        