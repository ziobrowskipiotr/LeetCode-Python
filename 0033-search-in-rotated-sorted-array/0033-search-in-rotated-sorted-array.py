class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            while left<=right:
                mid = (left+right)//2
                if target == nums[mid]:
                    return mid
                else:
                    if target > nums[mid]:
                        left = mid+1
                    else:
                        right = mid-1
            else:
                return -1

        left = 0
        right = len(nums)-1
        pivot = 0
        while left<=right:
            pivot = (left+right)//2
            if nums[pivot] > nums[-1]:
                left = pivot+1
            else:
                right = pivot-1

        if target <= nums[-1]:
            right = len(nums)-1
            return binary_search(left, right)
        else:
            right = left-1
            left = 0
            return binary_search(left, right)