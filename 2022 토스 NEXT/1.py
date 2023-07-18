# 37m

import sys
sys.setrecursionlimit(10**6)

import math
from itertools import combinations

def solution(n, m):
    VERBOSE = True
    def log(*msg):
        if VERBOSE: print(*msg)
    # -----------------------------

    """
    n이 2, 3, 4 중 하나
    1) n=2
        [1, m] : 소수
    2) n=3
        [1, sqrt(m)==p, m]  # [1, 2, 4], [1, 3, 9], [1, 5, 25]
    3) n=4
        [1, p, m//p, m]
    """

    # 1. 소수 구하기
    # def get_primes(num):
    #     flag = [True] * (num + 1)
    #     flag[0] = flag[1] = False
    #     for i in range(2, int(math.sqrt(num) + 1)):
    #         if flag[i]:
    #             j = 2
    #             while (i * j) <= num:
    #                 flag[i * j] = False
    #                 j += 1
    #     return [i for i, f in enumerate(flag) if f]
    # MAX_VAL = 1000000
    # primes = get_primes(MAX_VAL)

    def get_primes(num):
        rst = []
        target = 2
        while True:
            for i in range(2, int(math.sqrt(target))+1):
                if target % i == 0:
                    break
            else:
                rst.append(target)
                if len(rst) == num:
                    break
            target += 1
        return rst
    primes = get_primes(3000)


    # 2. Case handling
    if n == 2:
        log(primes[:m])
        return primes[m-1]
    elif n == 3:
        log(primes[:m])
        return primes[m-1]**2
    elif n == 4:
        s1 = {p1*p2 for p1, p2 in combinations(primes, 2)}
        s2 = {p1**3 for p1 in primes}
        s = sorted(s1 | s2)
        log(s[:m])
        return s[m-1]

# n = 3
# m = 3

# n = 4
# m = 5

n = 3
m = 3000

print(solution(n, m))
