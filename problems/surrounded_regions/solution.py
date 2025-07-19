class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        q = deque()

        for i in range(m):
            if board[i][0] == 'O':
                q.append((i, 0))
            if board[i][n - 1] == 'O':
                q.append((i, n - 1))
        for j in range(n):
            if board[0][j] == 'O':
                q.append((0, j))
            if board[m - 1][j] == 'O':
                q.append((m - 1, j))
        while q:
            i, j = q.popleft()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'T'
                q.extend([(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
        