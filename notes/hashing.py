from itertools import product
from bisect import bisect_left, insort_left
from collections import defaultdict
def example1(info, query):
    VERBOSE = True
    def log(*msg):
        if VERBOSE: print(*msg)
    # -----------------------------

    # 1. Save hash table
    cache = defaultdict(list)
    for vals in (row.split() for row in info):  # vals: ['java', 'backend', 'junior', 'pizza', '150']
        *vals, score = vals
        vals = [(val, '-') for val in vals]  # vals: [('java', '-'), ('backend', '-'), ('junior', '-'), ('pizza', '-')]
        for cond in product(*vals):
            insort_left(cache[cond], int(score))

    # 2. Process query
    answer = []
    for val_l, val_j, val_c, val_fs in map(lambda x: x.split(' and '), query):  # O(10만)
        val_f, val_s = val_fs.split()
        cond = (val_l, val_j, val_c, val_f)

        # 3. Binary search
        n_valids = len(cache[cond]) - bisect_left(cache[cond], int(val_s))
        answer.append(n_valids)

    return answer
