# VERBOSE = False
VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None


from itertools import product

maps   = None
n_rows = None
n_cols = None


from collections import deque

def bfs(graph: dict, src: int):
    traversal = [src]
    paths     = {src: [src]}
    q         = deque([[src, [src]]])  # cur, path

    while q:
        cv, cp = q.popleft()  # cv: cur_v, cp: cur_path
        for nv, w in graph[cv]:  # nv: next_v
            if nv not in paths:
                traversal.append(nv)
                paths[nv] = cp + [nv]
                q.append([nv, paths[nv]])
    return traversal, paths


def get_id(y, x):
    return n_cols*y + x

def get_adjs(y, x):
    adjs = []
    for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        nx, ny = x + dx, y + dy
        if ((ny < 0) or (n_rows <= ny)) or ((nx < 0) or (n_cols <= nx)):
            continue
        if maps[ny][nx] == 1:
            adjs.append((get_id(ny, nx), 1))
    return adjs

def solution(maps_):
    global maps, n_rows, n_cols
    maps   = maps_
    n_rows = len(maps)
    n_cols = len(maps[0])

    # 1. Generate graph
    graph = {}
    for x, y in product(range(n_cols), range(n_rows)):
        if maps[y][x] == 1:
            graph[get_id(y, x)] = get_adjs(y, x)

    # 2. BFS
    traversal, paths = bfs(graph, 0)
    if (target := get_id(n_rows-1, n_cols-1)) in paths:
        return len(paths[target])
    else:
        return -1


args = [
    [[1,0,1,1,1],
     [1,0,1,0,1],
     [1,0,1,1,1],
     [1,1,1,0,1],
     [0,0,0,0,1]]
]
print(solution(*args))
