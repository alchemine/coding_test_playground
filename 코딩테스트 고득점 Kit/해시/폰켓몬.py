VERBOSE = False
# VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None


def solution(nums):
    n_half = len(nums) // 2
    log(set(nums))
    n = len(set(nums))
    return min(n_half, n)

args = [
    [3,3,3,2,2,4]
]
print(solution(*args))
