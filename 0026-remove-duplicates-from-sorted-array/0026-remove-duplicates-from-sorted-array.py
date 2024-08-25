class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        j = 1
        while(j<len(nums)):
            if nums[i] == nums[j]:
                j+=1
            else:
                i+=1
                nums[i] = nums[j]
                j+=1
        return i+1
