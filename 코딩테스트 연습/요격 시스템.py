# VERBOSE = False
VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None

from collections import Counter

def solution(targets):
    vals = []
    for val in targets:
        vals.extend(val)
    max_val = max(vals)
    arr     = max_val*[0]

    starts = sorted(s for s, e in targets)
    ends   = sorted(e for s, e in targets)

    table = {}
    cnts   = Counter(starts)
    prev_t = None
    for cur_t in cnts:
        table[cur_t] = table[prev_t] + cnts[cur_t] if prev_t is not None else cnts[cur_t]
        prev_t = cur_t

    # start is not included
    for t in table:
        table[t] -= 1

    cnts = Counter(ends)
    for

    return table

args = [
    [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
]
print(solution(*args))
