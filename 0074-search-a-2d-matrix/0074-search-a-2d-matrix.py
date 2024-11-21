class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1
        pivot = 0
        while left <= right:
            pivot = (left+right)//2
            if target <= matrix[pivot][len(matrix[pivot])-1] and target >= matrix[pivot][0]:
                break
            else:
                if target > matrix[pivot][len(matrix[pivot])-1]:
                    left = pivot+1
                else:
                    right = pivot-1
        else:
            return False

        left = 0
        right = len(matrix[pivot])-1
        while left <= right:
            mid = (left+right)//2
            if target == matrix[pivot][mid]:
                return True
            else:
                if target > matrix[pivot][mid]:
                    left = mid+1
                else:
                    right = mid-1
        else:
            return False