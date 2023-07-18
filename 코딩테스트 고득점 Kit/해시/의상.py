VERBOSE = False
# VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None


from collections import defaultdict
import math

def solution(clothes):
    log(clothes)

    tables = defaultdict(list)
    for val, key in clothes:
        tables[key].append(val)

    nums = [len(val) + 1 for val in tables.values()]
    return math.prod(nums) - 1

args = [
    [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
]
print(solution(*args))
