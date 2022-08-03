# Coding Test Notes

---

# 1. [Graph](notes/graph.py)
- `mat2list(mat, start=1, verbose=False)`
  - Adjacency matrix → Adjacency list
    ```
    adj_mat = [[0, 1, 0],
               [1, 0, 1],
               [0, 1, 0]]
    
    graph = mat2list(adj_mat)
    
    # {1: [(2, 1)],
    #  2: [(1, 1), (3, 1)],
    #  3: [(2, 1)]}
    ```

- `dfs(graph, src)`
  - Depth First Search
  - $O(V+E)$

- `bfs(graph, src)`
  - Breadth First Search
  - $O(V+E)$

- `dijkstra(graph, src)`
  - Shortest path from `src` to the others
  - Only handle **positive** edges
  - $O((V+E)log V)$

- `floyd_warshall(graph)`
  - Shortest path from all the each other
  - Can handle **negative, positive** edges
  - $O(V^3)$

- `kruskal(graph)`
  - Minimum Spanning Tree
  - $O(E log E)$

- `backtracking(info, edges)`
  - Backtracking example ([2022 KAKAO BLIND RECRUITMENT - 양과 늑대](https://school.programmers.co.kr/learn/courses/30/lessons/92343))


# 2. [Dynamic Programming](notes/dynamic_programming.py)
- `bottom_up(n)`
  - Fibonacci example
  - **Loop** implementation
  - `[1] → [2] → ... → [n]` 

- `top_down(n, cache)`
  - Fibonacci example
  - **Recursive** implementation
  - `[n] → [n-1] → ... → [1]` 


# 3. [Matrix](notes/matrix.py)
- `rotate_outside(mat, r1, r2, c1, c2, clockwise=True)`
  - Rotate **outside** of the matrix for selected partition

- `rotate(mat, r1, r2, c1, c2, clockwise=True)`
  - Rotate **inside and outside** of the matrix for selected partition
