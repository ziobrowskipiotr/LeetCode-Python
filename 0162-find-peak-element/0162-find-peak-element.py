class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left<right:
            pivot = (left+right)//2        
            if nums[pivot] > nums[pivot-1] and nums[pivot] > nums[pivot+1]:
                return pivot
            else:
                if nums[pivot] <= nums[pivot+1]:
                    left = pivot+1
                else:
                    right = pivot-1
        return left