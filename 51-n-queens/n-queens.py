class Solution(object):
    def solveNQueens(self, n):
        res = []
        board = [['.'] * n for _ in range(n)]
        cols = set()
        d1 = set()
        d2 = set()
        def bTrack(row):
            if row == n:
                res.append([''.join(r) for r in board])
                return
            for col in range(n):
                if col in cols or row - col in d1 or row + col in d2:
                    continue
                board[row][col] = 'Q'
                cols.add(col)
                d1.add(row - col)
                d2.add(row + col)

                bTrack(row + 1)

                board[row][col] = '.'
                cols.remove(col)
                d1.remove(row - col)
                d2.remove(row + col)

        bTrack(0)
        return res