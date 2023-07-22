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

- `backtracking_example1(info, edges)`
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

- `update_rows_cols(mat)`
  - Update rows, cols of mat


# 4. [Hashing](notes/hashing.py)
- `example1()`
  > 적은 데이터 개수 + 문자열 + `dict()` → **hashing**


# 5. [Regular Expression](notes/regular_expression.ipynb)
- [Regular expression](https://alchemine.github.io/2021/10/27/re.html) 참고


# 6. [Tree](notes/tree.py)
- `Node`
  - `id, e, l, r`을 attribute로 가지는 class
- `preorder(node, traversal)`
  - 전위순회
  - Root -> **Left** -> Right
- `inorder(node, traversal)`
  - 중위순회
  - Left -> **Root** -> Right
- `postorder(node, traversal)`
  - 후위순회
  - Left -> **Right** -> Root


# 7. Hash
- **key**를 어떻게 설정할 지가 포인트.
- 문제에 힌트가 있는 경우가 있다.

# 8. Stack
- **Pair**가 존재하고, `push`, `pop`을 어떻게 구현할 지가 포인트.
