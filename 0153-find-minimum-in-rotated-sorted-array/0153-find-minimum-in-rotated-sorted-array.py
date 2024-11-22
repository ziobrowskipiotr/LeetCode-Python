class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            pivot = (left+right)//2
            if nums[pivot] > nums[-1]:
                left = pivot+1
            else:
                right = pivot-1
        return nums[left]