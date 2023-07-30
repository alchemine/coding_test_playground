# 3h 10m

# VERBOSE = False
VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None

import math

def validate(s):
    # 1. number of binary
    l = len(s)
    cond1 = (math.log2(l+1) % 1 == 0) or (math.log2(l+2) % 1 == 0)

    # 2. contains 1
    cond2 = '0' not in s[-2::-2]

    return int(cond1 and cond2)


def solution(numbers):
    answer = []
    for number in numbers:
        bin_str = bin(number)[2:]
        rst_val = validate(bin_str)
        answer.append(rst_val)
    return answer

args = [
    # [7, 42, 5]
    [63, 111, 95]
]
print(solution(*args))
