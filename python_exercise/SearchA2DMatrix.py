"""
Input: m by n matrix, each row/column is sorted
m == matrix.length, n == matrix[i].length
1 <= m, n <= 100
Output: True / False

case 1: [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
null case: []

Don't treat it as a 2D matrix, just treat it as a sorted list
matrix[x][y] => a[x * m + y]
a[x] => matrix[x / m][x % m]
"""

class Solution0:
    def searchMatrix(self, matrix, target):

        if not matrix or not matirx[0]:
            return False

        n = len(matrix)
        m = len(matrix[0])
        l, r = 0, m*n - 1

        while(l < r):
            mid = (l + r - 1) // 2 #  // 2
            if (matrix[mid / m][mid % m] < target):
            # if a[x] < target
                l = mid + 1
            else:
                r = mid

        return matrix[r / m][r % m] == target

class Solution1:
    def searchMatrix(self, matrix, target):
        """
        选取矩阵右上角的数字
        如果等于目标数字，结束查找
        如果大于目标数字，剔除该数字所在列（均比该数字大）
        如果小于目标数字，剔除该数字所在行（均比该数字小）
        """
        rows = len(matrix)
        columns = len(matrix[0])
        found = False

        if (matrix != None and rows > 0 and columns > 0):
            row, column = 0, columns - 1
            while (row < rows and columns > 0):
                #if (matrix[row * columns + column] == target):
                if (matrix[row][column] == target)
                # 从右上角开始
                    found = True
                    break
                elif (matrix[row][column] > target):
                    column -= 1
                else:
                    row += 1
        return found
