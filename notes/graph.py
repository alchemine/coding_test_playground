def mat2list(mat: list, start=1, verbose=False):
    """Adjacency matrix → Adjacency list
    - O(V^2)

    Args:
        mat: list
            Adjacency matrix
        start: int
            Start number
        verbose: bool
            Print output or not

    Returns: dict
        Adjacency list
    """
    rst = {}
    for cur_v, next_vs in enumerate(mat, start=start):
        rst[cur_v] = [(next_v, weight) for next_v, weight in enumerate(next_vs, start=start) if weight > 0]
    if verbose:
        print("cur_v : [(next_v, weight)]")
        for cur_v in rst:
            print(cur_v, ':', rst[cur_v])
    return rst


def dfs(graph: dict, src: int):
    """Depth First Search.
    - O(V+E)

    Args:
        graph: dict
            Adjacency list
        src: int
            Source node

    Returns:
        traversal: list
        paths: dict
    """
    paths     = {src: [src]}
    traversal = [src]
    s         = [[src, paths[src]]]  # (node, path)
    while s:
        cur_v, cur_path = s.pop()
        for next_v, w in graph[cur_v]:
            if next_v in paths:
                continue
            paths[next_v] = cur_path + [next_v]
            traversal.append(next_v)
            s.append([next_v, paths[next_v]])
    return paths, traversal


from collections import deque
def bfs(graph: dict, src: int):
    """Breadth First Search.
    - O(V+E)

    Args:
        graph: dict
            Adjacency list
        src: int
            Source node

    Returns:
        traversal: list
        paths: dict
    """
    paths     = {src: [src]}
    traversal = [src]
    q         = deque([[src, paths[src]]])  # (node, path)
    while q:
        cur_v, cur_path = q.popleft()
        for next_v, w in graph[cur_v]:
            if next_v in paths:
                continue
            paths[next_v] = cur_path + [next_v]
            traversal.append(next_v)
            q.append([next_v, paths[next_v]])
    return paths, traversal


from math import inf
from heapq import heappush, heappop
def dijkstra(graph: dict, src: int):
    """Dijkstra algorithm.
    Get the shortest path from `src` to the others.

    - O((V+E)log V)
    - Only handle positive edges

    Args:
        graph: dict
            Adjacency list
        src: int
            Source node

    Returns:
        dists: dict
        paths: dict
    """
    paths = {src: [src]}
    dists = {v: inf for v in graph}
    q     = []
    heappush(q, [0, src, paths[src]])  # [priority(distance), node, path]
    while q:
        cur_dist, cur_v, cur_path = heappop(q)
        if cur_dist >= dists[cur_v]:
            continue
        dists[cur_v] = cur_dist
        paths[cur_v] = cur_path
        for next_v, w in graph[cur_v]:
            heappush(q, [dists[cur_v] + w, next_v, paths[cur_v] + [next_v]])
    return paths, dists


from math import inf
from itertools import product
def floyd_warshall(graph):
    """Floyd Warshall algorithm.
    Get the shortest path from all the each other.

    - O(V^3)
    - Handle positive, negative edges

    Args:
        graph: dict
            Adjacency list

    Returns:
        dists: dict
    """
    dists = {start: {end: inf for end in graph} for start in graph}  # [v1][v2]: min distance of v1 -> v2
    for cur_v in graph:
        dists[cur_v][cur_v] = 0
        for next_v, w in graph[cur_v]:
            dists[cur_v][next_v] = w

    for mid in graph:
        for cur_v, next_v in product(graph, graph):
            dists[cur_v][next_v] = min(dists[cur_v][next_v], dists[cur_v][mid] + dists[mid][next_v])
    return dists


from heapq import heappush, heappop
def kruskal(graph: dict):
    """Kruskal algorithm.
    Get the minimum distance spanning every node.

    - O(ElogE)

    c.f. Prim algorithm: O(V^2)
    - Kruskal: appropriate for sparse graph
    - Prim: appropriate for dense graph

    Args:
        graph: dict
            Adjacency list

    Returns:
        dist:
    """
    def get_parent(parents, x):
        if parents[x] != x:
            parents[x] = get_parent(parents, parents[x])
        return parents[x]
    def union_parents(parents, a, b):  # union to min parent
        pa, pb = get_parent(parents, a), get_parent(parents, b)
        parents[pb] = pa if pa < pb else parents[pb]
        parents[pa] = pb if pa > pb else parents[pa]

    edges = []
    for v1 in graph:
        for v2, w in graph[v1]:
            heappush(edges, [w, v1, v2])

    parents = set(graph)
    dist    = 0
    while edges:
        w, v1, v2 = heappop(edges)
        if get_parent(parents, v1) != get_parent(parents, v2):
            union_parents(parents, v1, v2)
            dist += w
    return dist


def backtracking_example1(info, edges):
    # https://school.programmers.co.kr/learn/courses/30/lessons/92343
    answer = 0
    N = len(info)
    graph = [[] for _ in range(N)]

    for start, end in edges:
        graph[start].append(end)

    stack = [(1, 0, [0])]
    while stack:
        cur_sheep, cur_wolf, visited = stack.pop()
        answer = max(answer, cur_sheep)

        for cur_node in visited:  # 만난 모든 node들에 대하여 다시 처음부터 탐색
            for next_node in graph[cur_node]:  # cur_node와 연결된 모든 node들에 대하여
                if next_node not in visited:  # 만나지 않았다면
                    next_sheep = cur_sheep + info[next_node]^1
                    next_wolf  = cur_wolf + info[next_node]
                    if next_sheep <= next_wolf:
                        continue  # invalid
                    stack.append((next_sheep, next_wolf, visited + [next_node]))  # 가능한 모든 경우를 저장
    return answer
