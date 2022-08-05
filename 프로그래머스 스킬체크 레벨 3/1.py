# 27m

import sys
sys.setrecursionlimit(10**6)

def solution(n, build_frame):
    VERBOSE = True
    def log(*msg):
        if VERBOSE: print(*msg)
    # -----------------------------

    # 1. Build rows, cols
    rows = set()
    cols = set()

    def is_valid(x, y, a, rows, cols):
        """(x, y)에 있는 a가 valid한지 체크"""
        if a == 0:
            cond1 = (y == n)  # 기둥은 바닥 위에 있거나
            cond2 = ((x, y) in rows) or ((x - 1, y) in rows)  # 보의 한쪽 끝 부분 위에 있거나
            cond3 = (x, y + 1) in cols  # 다른 기둥 위에 있어야 합니다
            return any([cond1, cond2, cond3])
        else:
            cond1 = ((x, y + 1) in cols) or ((x + 1, y + 1) in cols)  # 한쪽 끝 부분이 기둥 위에 있거나
            cond2 = ((x - 1, y) in rows) and ((x + 1, y) in rows)  # 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다
            return any([cond1, cond2])

    def process(x, y, a, b, rows, cols):
        if a == 0:  # col
            if b == 0:  # del
                tmp_cols = cols - {(x, y)}

                conds = []
                if (x-1, y-1) in rows:
                    conds.append(is_valid(x - 1, y - 1, 1, rows, tmp_cols))  # 기둥의 윗 왼쪽 보
                if (x, y-1) in rows:
                    conds.append(is_valid(x, y-1, 1, rows, tmp_cols))        # 기둥의 윗 오른쪽 보
                if (x, y-1) in tmp_cols:
                    conds.append(is_valid(x, y - 1, 0, rows, tmp_cols))     # 윗 기둥
                if all(conds):
                    cols.remove((x, y))
            else:  # ins
                if is_valid(x, y, a, rows, cols):
                    cols.add((x, y))
        elif a == 1:  # row
            if b == 0:  # del
                tmp_rows = rows - {(x, y)}

                conds = []
                if (x-1, y) in tmp_rows:
                    conds.append(is_valid(x-1, y, 1, tmp_rows, cols))  # 왼쪽 보
                if (x, y) in cols:
                    conds.append(is_valid(x, y, 0, tmp_rows, cols))    # 왼쪽 기둥
                if (x+1, y) in cols:
                    conds.append(is_valid(x+1, y, 0, tmp_rows, cols))  # 오른쪽 기둥
                if (x+1, y) in tmp_rows:
                    conds.append(is_valid(x+1, y, 1, tmp_rows, cols))  # 오른쪽 보
                if all(conds):
                    rows.remove((x, y))
            else:  # ins
                if is_valid(x, y, a, rows, cols):
                    rows.add((x, y))


    for x, y, a, b in build_frame:
        y = n - y  # convert y-axis
        process(x, y, a, b, rows, cols)
        log("rows:", rows, "cols:", cols)


    # 2. Generate output
    rows = [(x, n-y, 1) for x, y in rows]
    cols = [(x, n-y, 0) for x, y in cols]
    answer = rows + cols
    return sorted(answer)


n = 5
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
print(solution(n, build_frame))
