from itertools import product
from math import inf

def get(cycle, idx):
    return cycle[idx % len(cycle)]

def solution(n, weak, dist):
    VERBOSE = True
    def log(*msg):
        if VERBOSE: print(*msg)
    # -----------------------------

    # weak <= 15, dist <= 8 -> brute force, backtracking?
    weak = tuple(weak)
    dist = tuple(dist)
    n_friends = inf

    walls = list(range(n))
    stack = {(weak, dist)}

    while stack:
        log(stack)
        cur_weak, cur_dist = stack.pop()
        max_dist  = cur_dist[-1]
        next_dist = cur_dist[:-1]

        cur_n_friends = len(dist) - len(next_dist)
        if n_friends <= cur_n_friends:
            continue

        for pos, clockwise in product(cur_weak, [True, False]):
            # Search weaks
            if clockwise:
                searched_weaks = [get(walls, pos+i) for i in range(max_dist+1)]
            else:
                searched_weaks = [get(walls, pos-i) for i in range(max_dist+1)]
            next_weak = tuple(w for w in cur_weak if w not in searched_weaks)

            if len(next_weak) == 0:  # success
                n_friends = cur_n_friends
                continue
            elif len(next_dist) == 0:  # failure
                continue

            stack.add((next_weak, next_dist))

    if n_friends == inf:
        n_friends = -1

    return n_friends

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
# weak = [1, 3, 4, 9, 10]
# dist = [3, 5, 7]
# weak = [0, 2, 4, 5, 9]
# dist = [1, 2, 2, 3]
print(solution(n, weak, dist))
