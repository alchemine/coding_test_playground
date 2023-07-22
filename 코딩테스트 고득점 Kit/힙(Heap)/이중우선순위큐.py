# VERBOSE = False
VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None


from queue import PriorityQueue
from collections import defaultdict

def init():
    min_Q, max_Q = PriorityQueue(), PriorityQueue()
    L = cnt_min = cnt_max = 0
    sync = defaultdict(int)
    return min_Q, max_Q, L, cnt_min, cnt_max, sync

def solution(operations):
    min_Q, max_Q, L, cnt_min, cnt_max, sync = init()

    # ["I 16", "D -1", "D 1"] -> [('I', 16), ('D', -1), ('D', 1)]
    for op, val in [(op, int(val)) for op, val in map(lambda x: x.split(), operations)]:
        if op == 'I':
            min_Q.put(val), max_Q.put(-val)
            sync[val] += 1
            L += 1
        elif op == 'D' and val in [1, -1]:
            if cnt_min + cnt_max == L:
                continue
            if val == 1:
                while True:
                    max_val = -max_Q.get()
                    if sync[max_val] > 0:
                        break
                cnt_max += 1
                sync[max_val] -= 1
            else:
                while True:
                    min_val = min_Q.get()
                    if sync[min_val] > 0:
                        break
                cnt_min += 1
                sync[min_val] -= 1
        else:
            raise ValueError

        log("min_Q:", min_Q.queue)
        log("max_Q:", max_Q.queue)
        log("sync:", sync)

    if cnt_min + cnt_max == L:
        return [0, 0]
    else:
        while True:
            max_val = -max_Q.get()
            if sync[max_val] > 0:
                break
        while True:
            min_val = min_Q.get()
            if sync[min_val] > 0:
                break
        return [max_val, min_val]

args = [
    # ["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]
    # ["I 2","I 4","D -1", "I 1", "D 1"]
    # ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
    ["I 3", "I 2", "I 1", "D 1", "D 1", "I 3", "D -1"]
]
print(solution(*args))
