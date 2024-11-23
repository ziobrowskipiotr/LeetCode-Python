class Solution:
	def maxArea(self, height: List[int]) -> int:
		left = 0
		right = len(height)-1
		max_area = 0
		high = 0
		while left < right:
			if height[left] > height[right]:
				high = height[right]
			else:
				high = height[left]
			current_area = high*(right-left)
			if current_area > max_area:
				max_area = current_area
			if height[left] >= height[right]:
				right -= 1
			else:
				left += 1
		return max_area