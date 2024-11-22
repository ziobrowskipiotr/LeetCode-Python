class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge_list = []
        left = 0
        right = 0
        while left < len(nums1) and right < len(nums2):
            if nums1[left] >= nums2[right]:
                merge_list.append(nums2[right])
                right += 1
            else:
                merge_list.append(nums1[left])
                left += 1
        else:
            if right == len(nums2):
                merge_list += nums1[left:]
            else:
                merge_list += nums2[right:]

        if len(merge_list)%2 == 0:
            return (merge_list[(len(merge_list)-1)//2] + merge_list[len(merge_list)//2])/2
        else:
            return merge_list[(len(merge_list)-1)//2]