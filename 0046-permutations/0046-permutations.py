class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current_list = []

        def backtrack():
            if len(current_list) == len(nums):
                result.append(current_list[:])
            else:
                for element in nums:
                    if element not in current_list:
                        current_list.append(element)
                        backtrack()
                        current_list.pop()
                    else:
                        continue
        backtrack()
        return result