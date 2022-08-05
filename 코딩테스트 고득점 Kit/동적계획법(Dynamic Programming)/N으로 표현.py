import sys
sys.setrecursionlimit(10**6)

cache = {}  # [x]: N을 x개 사용하여 만들 수 있는 집합

def solution(N, number):
    VERBOSE = True
    def log(*msg):
        if VERBOSE: print(*msg)
    # -----------------------------

    def concat(N, n):
        return int(str(N)*n)
    def compute_ops(N, cache1, cache2):
        rst1 = set.union(*[{x+N, x-N, x*N, x//N} for x in cache1])
        if cache2 is None:
            return rst1
        else:
            rst2 = set.union(*[{x + (N*N), x + (N//N),
                                x - (N*N), x - (N//N),
                                x * (N+N), x * (N-N),
                                x // (N + N), # x // (N - N),
                                x // (N * N), x // (N // N)
                                } for x in cache2])
            return set.union(rst1, rst2)

    # 1. Basis
    if number == N:
        return 1
    cache[1] = {N}
    cache[2] = compute_ops(N, cache[1], None) | {concat(N, 2)}


    # 2. DP
    for i in range(3, 9):
        cache[i] = compute_ops(N, cache[i-1], cache[i-2]) | {concat(N, i)}
        if number in cache[i]:
            for c in cache:
                log(c, ':', cache[c])
            return i
    return -1


N = 5
number = 12
print(solution(N, number))
