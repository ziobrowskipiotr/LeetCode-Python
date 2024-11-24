class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        result = float('inf')
        sum_cur_window = 0
        for right in range(len(nums)):
            sum_cur_window += nums[right]
            while sum_cur_window >= target:
                result = min(result, right-left+1)
                sum_cur_window -= nums[left]
                left += 1
        return result if result < float('inf') else 0
