class UniquePaths:
    def get_number_of_unique_paths(self, m: int, n: int):
        matrix = [[0] * n] * m

        for r in range(m):
            matrix[r][0] = 1

        matrix[0] = [1] * n

        for row in range(1, m):
            for column in range(1, n):
                matrix[row][column] = matrix[row - 1][column] + matrix[row][column - 1]

        return matrix[m - 1][n - 1]
