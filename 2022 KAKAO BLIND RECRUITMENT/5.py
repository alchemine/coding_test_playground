# 00m ->

def solution(info, edges):
    VERBOSE = True
    def log(*msg):
        if VERBOSE: print(*msg)
    # -----------------------------

    answer = 0
    N = len(info)
    graph = [[] for _ in range(N)]

    for p, c in edges:
        graph[p].append(c)

    stack = [(1, 0, [0])]
    while stack:
        cur_sheep, cur_wolf, visited = stack.pop()
        answer = max(answer, cur_sheep)

        for cur_node in visited:  # 만난 모든 node들에 대하여 재탐색
            for next_node in graph[cur_node]:  # cur_node와 연결된 모든 node들에 대하여
                if next_node not in visited:  # 만나지 않았다면
                    next_sheep = cur_sheep
                    next_wolf = cur_wolf
                    next_wolf  += info[next_node]
                    next_sheep += info[next_node]^1

                    if next_sheep <= next_wolf:
                        continue  # invalid
                    stack.append((next_sheep, next_wolf, visited + [next_node]))

    return answer



# info  = [0,0,1,1,1,0,1,0,1,0,1,1]
# edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

info = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]
print(solution(info, edges))
