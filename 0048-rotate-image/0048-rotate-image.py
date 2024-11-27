class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left = 0
        right = len(matrix)-1
        top = 0
        bottom = len(matrix)-1

        while left<right:
            for i in range(right-left):
                matrix[top+i][right], matrix[bottom][right-i], matrix[bottom-i][left], matrix[top][left+i] = matrix[top][left+i], matrix[top+i][right], matrix[bottom][right-i], matrix[bottom-i][left]
            right -= 1
            left += 1
            top += 1
            bottom -= 1
