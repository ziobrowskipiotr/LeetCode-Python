class Solution:
    def find2sum(self, nums, result, target):
        left = target+1
        right = len(nums)-1
        while left<right:
            if nums[left] + nums[right] == -nums[target]:
                result.append([nums[target], nums[left], nums[right]])
                left += 1
                right -= 1
                while left<right and nums[left-1] == nums[left]:
                    left += 1
            elif nums[left] + nums[right] > -nums[target]:
                right -= 1
            else:
                left += 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        def quicksort(nums, left, right):
            if left < right:
                pivot_ix = partition(nums, left, right)
                quicksort(nums, left, pivot_ix-1)
                quicksort(nums, pivot_ix+1, right)

        def partition(nums, left, right):
            pivot = nums[left]
            low = left
            for i in range(left+1, right+1):
                if nums[i] < pivot:
                    low += 1
                    nums[i], nums[low] = nums[low], nums[i]
            nums[low], nums[left] = nums[left], nums[low]
            return low
        
        quicksort(nums, 0, len(nums)-1)
        for i in range(len(nums)):
            if i==0 or nums[i-1] != nums[i]:
                self.find2sum(nums, result , i)
        return result

