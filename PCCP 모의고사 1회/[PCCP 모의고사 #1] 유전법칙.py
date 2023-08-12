# 30m -> 59m

VERBOSE = False
# VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None


def solution(queries):
    return [solution_one(idx_gen, idx_order) for idx_gen, idx_order in queries]

def solution_one(idx_gen, idx_order):
    if (idx_gen == 1) and (idx_order == 1):
        return 'Rr'

    # 1. Find parents
    idx_orders = (1+idx_gen)*[None]
    idx_orders[1] = 1

    cur_idx_order = idx_order
    for ig in range(idx_gen, 0, -1):  # idx_gen: 3
        idx_orders[ig] = cur_idx_order % 4
        cur_idx_order = 1 + (cur_idx_order-1) // 4
    log(idx_order, idx_orders)


    # 2. Find child
    parent = 'Rr'
    for ig in range(2, idx_gen+1):
        idx_order_child = idx_orders[ig]-1  # [1, 2, 3, 4] -> [0, 1, 2, 3]
        if parent == 'RR':
            childs = ['RR', 'RR', 'RR', 'RR']
        elif parent == 'Rr':
            childs = ['RR', 'Rr', 'Rr', 'rr']
        elif parent == 'rr':
            childs = ['rr', 'rr', 'rr', 'rr']
        else:
            raise ValueError
        child  = childs[idx_order_child]
        parent = child
        log(child)
    return child

args = [
    [[3, 1], [2, 3], [3, 9]]
    # [[3, 9]]
]
print(solution(*args))
