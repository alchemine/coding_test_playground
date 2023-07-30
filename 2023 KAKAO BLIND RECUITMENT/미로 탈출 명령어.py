# VERBOSE = False
VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None


def solution(n, m, x, y, r, c, k):
    nx, ny = m, n
    s, e   = (y, x), (c, r)  # start, end point
    dx, dy = e[0] - s[0], e[1] - s[1]

    sx = abs(dx) * ('l' if dx < 0 else 'r')
    sy = abs(dy) * ('u' if dy < 0 else 'd')
    min_path = sx + sy
    min_len  = len(min_path)
    if min_len > k:
        return 'impossible'
    elif min_len == k:
        path_list = sorted(min_path)
    elif (k - min_len) % 2 == 0:
        n_iters = (k - min_len) // 2
        cands = [n_iters*"lr" + min_path, n_iters*"ud" + min_path]
        path  = min(cands)

    else:
        return 'impossible'

    return ''.join(path_list)

args = [
    3,	4,	2,	3,	3,	1,	5
]
print(solution(*args))
"dllrl"