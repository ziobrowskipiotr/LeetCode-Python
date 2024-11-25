class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        i = 0
        while i<len(nums):
            result.append(str(nums[i]))
            i += 1
            copy_i = i
            while i<len(nums) and nums[i] == nums[i-1]+1:
                i += 1
            else:
                if i != copy_i:
                    result[-1] += "->"+str(nums[i-1])
        return result