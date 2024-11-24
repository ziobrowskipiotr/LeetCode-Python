class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_num_ix = {}
        for i in range(len(nums)):
            if target-nums[i] in map_num_ix:
                return [map_num_ix[target-nums[i]], i]
            map_num_ix[nums[i]] = i
        return [-1, -1]
