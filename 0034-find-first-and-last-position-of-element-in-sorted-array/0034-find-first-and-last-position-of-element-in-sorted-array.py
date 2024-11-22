class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1,-1]
        left = 0
        right = len(nums)-1
        pivot = 0
        while left<=right:
            pivot = (left+right)//2
            if nums[pivot] == target:
                if pivot == 0 or nums[pivot-1] != target:
                    result[0] = pivot
                    break
                else:
                    right = pivot-1
            else:
                if target > nums[pivot]:
                    left = pivot+1
                else:
                    right = pivot-1
        else:
            return result
		
        left = pivot
        right = len(nums)-1
        while left<=right:
            pivot = (left+right)//2
            if nums[pivot] == target:
                if pivot == len(nums)-1 or nums[pivot+1] != target:
                    result[1] = pivot
                    break
                else:
                    left = pivot+1
            else:
                if target > nums[pivot]:
                    left = pivot+1
                else:
                    right = pivot-1
        return result
