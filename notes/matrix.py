def rotate_outside(mat, r1, r2, c1, c2, clockwise=True):
    if clockwise:
        # 1. 첫 번째 값 저장
        tmp = mat[r1][c1]

        # 2. 왼쪽 세로 업데이트
        for r in range(r1, r2):
            mat[r][c1] = mat[r + 1][c1]

        # 3. 아랫쪽 가로 업데이트
        for c in range(c1, c2):
            mat[r2][c] = mat[r2][c + 1]

        # 4. 오른쪽 세로 업데이트
        for r in range(r2, r1, -1):
            mat[r][c2] = mat[r - 1][c2]

        # 5. 위쪽 가로 업데이트
        for c in range(c2, c1, -1):
            mat[r1][c] = mat[r1][c - 1]

        # 6. 첫 번째 값 업데이트
        mat[r1][c1 + 1] = tmp
    else:
        # 1. 첫 번째 값 저장
        tmp = mat[r1][c1]

        # 2. 위쪽 가로 업데이트
        for c in range(c1, c2):
            mat[r1][c] = mat[r1][c + 1]

        # 3. 오른쪽 세로 업데이트
        for r in range(r1, r2):
            mat[r][c2] = mat[r + 1][c2]

        # 4. 아랫쪽 가로 업데이트
        for c in range(c2, c1, -1):
            mat[r2][c] = mat[r2][c - 1]

        # 5. 왼쪽 세로 업데이트
        for r in range(r2, r1, -1):
            mat[r][c1] = mat[r - 1][c1]

        # 6. 첫 번째 값 업데이트
        mat[r1 + 1][c1] = tmp


def rotate(mat, r1, r2, c1, c2, clockwise=True):
    # 1. 바깥쪽부터 시작하여 회전
    while (r2 > r1) and (c2 > c1):
        rotate_outside(mat, r1, r2, c1, c2, clockwise)
        r1 += 1
        r2 -= 1
        c1 += 1
        c2 -= 1


def update_rows_cols(mat):
    n_rows = len(mat)
    n_cols = len(mat[0])

    for i in range(n_rows):  # i'th row
        row = mat[i]
        for j in range(n_cols):
            mat[i][j] = row[j]

    for j in range(n_cols):  # j'th col
        col = [mat[i][j] for i in range(n_rows)]
        for i in range(n_rows):
            mat[i][j] = col[i]
