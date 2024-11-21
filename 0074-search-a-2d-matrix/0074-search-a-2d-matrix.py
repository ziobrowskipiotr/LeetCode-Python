class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def rows_search(left, right):
            if left > right:
                return -1
            pivot = (left+right)//2
            if target <= matrix[pivot][len(matrix[pivot])-1] and target >= matrix[pivot][0]:
                return pivot
            else:
                if target > matrix[pivot][len(matrix[pivot])-1]:
                    return rows_search(pivot+1, right)
                else:
                    return rows_search(left, pivot-1)
        def column_search(left,right, i):
            if left > right:
                return False
            pivot = (left+right)//2
            if target == matrix[i][pivot]:
                return True
            else:
                if target > matrix[i][pivot]:
                    return column_search(pivot+1, right, i)
                else:
                    return column_search(left, pivot-1, i)
        row_number = rows_search(0, len(matrix)-1)
        if row_number == -1:
            return False
        else:
            return column_search(0, len(matrix[row_number])-1, row_number)