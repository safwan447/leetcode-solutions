class Solution(object):
    def maximalSquare(self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        dp=[[0]*n for i in range(m)]
        maxx=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1' or matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    maxx = max(maxx, dp[i][j])
                else:
                    dp[i][j] = 0
        return maxx**2