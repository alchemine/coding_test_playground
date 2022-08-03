# 3:16 ->

import numpy as np

def solution(board, skill):
    VERBOSE = True
    def log(*msg):
        if VERBOSE: print(*msg)
    # -----------------------------

    # 1. Prepare cumsum matrix
    N, M = len(board), len(board[0])
    cumsum = np.zeros((N+1, M+1), dtype=np.int32)
    board  = np.asarray(board, dtype=np.int32)

    # 2. Fill cumsum matrix
    def fill_cumsum(cumsum):
        cumsum = cumsum.copy()
        # 1) Left -> Right
        for row in range(N):
            cumsum[row, :M] = cumsum[row, :M].cumsum()

        # 2) Up -> Down
        for col in range(M):
            cumsum[:N, col] = cumsum[:N, col].cumsum()

        return cumsum

    for type, r1, c1, r2, c2, degree in skill:
        degree = degree if type == 2 else -degree
        cumsum[r1][c1]     = degree
        cumsum[r1][c2+1]   = -degree
        cumsum[r2+1][c1]   = -degree
        cumsum[r2+1][c2+1] = degree


    # 3. Compute cumsum
    cumsum = fill_cumsum(cumsum)
    return np.sum((board + cumsum[:N, :M]) > 0)


board = [[5,5,5,5,5],
         [5,5,5,5,5],
         [5,5,5,5,5],
         [5,5,5,5,5]]

skill = [[1,0,0,3,4,4],
         [1,2,0,2,3,2],
         [2,1,0,3,1,2],
         [1,0,1,3,3,1]]
print(solution(board, skill))
