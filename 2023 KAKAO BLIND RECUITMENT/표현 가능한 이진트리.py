# 3h 10m

VERBOSE = False
# VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None

import math

def solution(numbers):
    answer = []
    # pos = [3] + [3+2**k for k in range(2, 10**4)]

    for number in numbers:
        num_bin = bin(number)[2:]
        L       = len(num_bin)

        cond1 = False
        if L % 2 == 0:
            if (L == 2) or (math.log2(L-2) % 1 == 0):
                cond1 = True
        else:
            if (L == 3) or (math.log2(L-3) % 1 == 0):
                cond1 = True

        mid   = num_bin[-2::-2]
        cond2 = '0' not in mid

        answer.append(1 if cond1 and cond2 else 0)
    return answer

args = [
    # [7, 42, 5]
    [63, 111, 95]
]
print(solution(*args))
