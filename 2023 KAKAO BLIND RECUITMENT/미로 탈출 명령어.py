# VERBOSE = False
VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None


from collections import Counter

CACHE = {}

def solution(n, m,
             x, y,
             r, c,
             k):
    go          = lambda _x, _y, dir: {'u': (_x - 1, _y), 'r': (_x, _y + 1), 'd': (_x + 1, _y), 'l': (_x, _y - 1)}[dir]
    is_valid_xy = lambda _x, _y: (1 <= _x <= n) and (1 <= _y <= m)

    def is_valid_path(path):
        if len(path) == 0:
            return True
        elif len(path) == 1:
            next_xy = go(x, y, path)
            if is_valid_xy(*next_xy):
                CACHE[path] = next_xy
                return True
            else:
                return False
        else:
            prev_path, dir = path[:-1], path[-1]
            prev_xy = CACHE[prev_path]
            next_xy = go(*prev_xy, dir)
            if is_valid_xy(*next_xy):
                CACHE[path] = next_xy
                return True
            else:
                return False

    def sol(cnt, path, rst):
        if len(rst) == 1:
            return
        if not is_valid_path(path):
            return
        if len(path) == k:
            rst.append(path)
            return
        for dir in ('d', 'l', 'r', 'u'):
            if cnt[dir] > 0:
                sol(cnt - Counter({dir: 1}), path + dir, rst)
        if path == '':
            rst.append('impossible')


    # (x, y) -> (r, c)
    shortest_path  = ''
    shortest_path += abs(x - r) * ('u' if x > r else 'd')
    shortest_path += abs(y - c) * ('l' if y > c else 'r')

    n_cycles, mod = divmod(k - len(shortest_path), 2)
    if mod == 1:
        return 'impossible'

    cands    = []
    cnt_base = Counter(shortest_path)
    for n_lr in range(n_cycles + 1):
        added_path = n_lr * "lr" + (n_cycles - n_lr) * "ud"
        cnt = cnt_base + Counter(added_path)
        rst = []
        sol(cnt, "", rst)
        cands.append(rst[0])
    return min(cands)


args = [
    3, 4, 2, 3, 3, 1, 5
    # 6, 6, 2, 6, 6, 5, 11
]
print(solution(*args))
