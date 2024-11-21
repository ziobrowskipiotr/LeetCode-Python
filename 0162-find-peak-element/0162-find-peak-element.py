class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left<right:
            pivot = (left+right)//2
            pivot_left = pivot-1
            pivot_right = pivot+1
            if pivot_right == len(nums):
                pivot_right = 0
            if nums[pivot] > nums[pivot_left] and nums[pivot] > nums[pivot_right]:
                return pivot
            else:
                if nums[pivot] <= nums[pivot_right]:
                    left = pivot_right
                else:
                    right = pivot_left
        return left
