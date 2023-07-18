import sys
sys.setrecursionlimit(10**6)

from itertools import combinations

def solution(arr):
    VERBOSE = False
    def log(*msg):
        if VERBOSE: print(*msg)
    # -----------------------------

    answer = 0

    def check_num_addictive_palindrome(sarr):
        # 1. sarr 의 길이가 1이거나
        # 2. sarr[:k] == sarr[g:] 인 경우, True
        if len(sarr) == 1:
            log(sarr)
            return True

        for k in range(1, n):
            for g in range(1, n):
                if k > g:
                    continue
                if sum(sarr[:k]) == sum(sarr[g:]):
                    log(sarr[:k], sarr[g:])
                    return True
        return False


    n = len(arr)
    for s, e in [(s, e) for s, e in combinations(list(range(n+1)), 2) if s+1 < e]:
        sarr = arr[s:e]
        log(sarr)
        if check_num_addictive_palindrome(sarr):
            answer += 1

    return answer

arr = [1, 2, 3, 1, 1, 1]
print(solution(arr))
