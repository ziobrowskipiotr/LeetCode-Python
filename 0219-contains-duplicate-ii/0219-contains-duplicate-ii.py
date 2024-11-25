class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                if i-hash_map[nums[i]] <= k:
                    return True
                else:
                    hash_map[nums[i]] = i
            else:
                hash_map[nums[i]] = i
        return False