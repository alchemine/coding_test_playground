import sys
sys.setrecursionlimit(10**6)

from itertools import accumulate

def solution(board, skill):
    VERBOSE = True
    def log(*msg):
        if VERBOSE: print(*msg)
    # -----------------------------

    # 1. Generate cumsum matrix
    N, M = len(board), len(board[0])
    cumsum = [(M+1)*[0] for _ in range(N+1)]

    # 2. Fill cumsum
    for type, r1, c1, r2, c2, degree in skill:
        degree = -degree if type == 1 else degree

        cumsum[r1][c1]     += degree
        cumsum[r2+1][c2+1] += degree
        cumsum[r1][c2+1]   += -degree
        cumsum[r2+1][c1]   += -degree

    # 3. Process cumsum
    # 1) Accumulate rows: ->
    for i in range(len(cumsum)):
        row = cumsum[i]  # i'th row
        cumsum[i] = list(accumulate(row))

    for j in range(len(cumsum[0])):
        col = [cumsum[i][j] for i in range(len(cumsum))]  # j'th col
        col_proc = list(accumulate(col))
        for i in range(len(cumsum)):
            cumsum[i][j] = col_proc[i]

    # 4. Get board
    answer = 0
    for i in range(N):
        for j in range(M):
            board[i][j] += cumsum[i][j]
            answer += (board[i][j] > 0)

    return answer

# board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
# skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]

print(solution(board, skill))
