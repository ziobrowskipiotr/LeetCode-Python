class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows_set = set()
        columns_set = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows_set.add(i)
                    columns_set.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows_set or j in columns_set:
                    matrix[i][j] = 0

                    

        