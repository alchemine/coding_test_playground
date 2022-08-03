# 32m -> 46m

import math

def solution(n, k):
    VERBOSE = True
    def log(*msg):
        if VERBOSE: print(*msg)
    # -----------------------------

    # 1. k진수로 변환
    def convert_base(n, q):
        rev_base = ''
        while n > 0:
            n, mod = divmod(n, q)
            rev_base += str(mod)
        return str(rev_base[::-1])
    base_k = convert_base(n, k)


    # 2. 0 기준으로 자르기
    vals = list(filter(lambda x: len(x) > 0, base_k.split('0')))

    # 3. 소수 판별
    def is_prime(x):
        x = int(x)
        if x < 2:
            return False

        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    return len(tuple(filter(is_prime, vals)))


# n = 437674
# k = 3
n = 110011
k = 10
print(solution(n, k))
