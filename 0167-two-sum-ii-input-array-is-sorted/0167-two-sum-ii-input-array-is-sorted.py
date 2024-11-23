class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        result = [-1, -1]
        while left < right:
            if numbers[left] + numbers[right] == target:
                result[0] = left+1
                result[1] = right+1
                return result
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return result
