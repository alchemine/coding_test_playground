# Adjacency matrix → Adjacency list
def mat2list(mat, start=1, verbose=False):  # O(V^2)
    rst = {}
    for cur_v, next_vs in enumerate(mat, start=start):
        rst[cur_v] = [(next_v, weight) for next_v, weight in enumerate(next_vs, start=start) if weight > 0]
    if verbose:
        print("cur_v : [(next_v, weight)]")
        for cur_v in rst:
            print(cur_v, ':', rst[cur_v])
    return rst


def dfs(graph, src):  # O(V+E)
    visited   = {src}
    traversal = [src]
    path      = {src: [src]}
    s         = [[src, [src]]]  # (node, path)
    while s:
        cur_v, cur_path = s.pop()
        for next_v, w in ((v, w) for v, w in graph[cur_v] if v not in visited):
            visited.add(next_v)
            traversal.append(next_v)
            path[next_v] = cur_path + [next_v]
            s.append([next_v, path[next_v]])
    return traversal, path


from collections import deque
def bfs(graph, src):  # O(V+E)
    visited   = {src}
    traversal = [src]
    path      = {src: [src]}
    q         = deque([[src, [src]]])  # (node, path)
    while q:
        cur_v, cur_path = q.popleft()
        for next_v, w in ((v, w) for v, w in graph[cur_v] if v not in visited):
            visited.add(next_v)
            traversal.append(next_v)
            path[next_v] = cur_path + [next_v]
            q.append([next_v, path[next_v]])
    return traversal, path


from heapq import heappush, heappop
from math import inf
def dijkstra(graph, src):  # O((V+E)log V)
    # Only handle positive edges
    dists = {v: inf for v in graph}
    paths = {src: [src]}
    q     = []
    heappush(q, [0, src, [src]])  # (dist: priority, node, path)
    while q:
        cur_dist, cur_v, cur_path = heappop(q)
        if cur_dist < dists[cur_v]:
            dists[cur_v] = cur_dist
            paths[cur_v] = cur_path
            for next_v, w in graph[cur_v]:
                heappush(q, [dists[cur_v] + w, next_v, paths[cur_v] + [next_v]])
    return dists, paths


from math import inf
from itertools import product
def floyd_warshall(graph):  # O(V^3)
    # Handle positive, negative edges
    dists = {start: {end: inf for end in graph} for start in graph}  # [v1][v2]: min distance of v1 -> v2
    for start in graph:
        dists[start][start] = 0
        for end, w in graph[start]:
            dists[start][end] = w

    for mid in graph:
        for start, end in product(graph, graph):
            dists[start][end] = min(dists[start][end], dists[start][mid] + dists[mid][end])
    return dists


def kruskal(graph):  # O(ElogE)
    def get_parent(parents, x):
        if parents[x] != x:
            parents[x] = get_parent(parents, parents[x])
        return parents[x]
    def union_parents(parents, a, b):  # union to min parent
        pa, pb = get_parent(parents, a), get_parent(parents, b)
        parents[pb] = pa if pa < pb else parents[pb]
        parents[pa] = pb if pa > pb else parents[pa]

    edges = []
    for start in graph:
        for end, w in graph[start]:
            edges.append((w, start, end))

    parents = set(graph)
    dist = 0
    for w, start, end in sorted(edges):
        if get_parent(parents, start) != get_parent(parents, end):
            union_parents(parents, start, end)
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
