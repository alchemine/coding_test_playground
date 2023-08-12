# 59m 40s -> 2h
# 32m

VERBOSE = False
# VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None


from queue import PriorityQueue

def solution(program):
    table = [PriorityQueue() for _ in range(11)]  # 10개의 점수 ([1] ~ [10])
    for score, start_time, exec_time in program:
        table[score].put((start_time, exec_time))  # priority: start_time

    answer   = 11*[0]
    cur_time = 0
    while True:
        min_start_time = None
        for score, Q in enumerate(table[1:], start=1):
            if not Q.empty():
                start_time     = Q.queue[0][0]    # Q.queue[0]: (start_time, exec_time) of highest priority
                min_start_time = min(min_start_time, start_time) if min_start_time is not None else start_time
                if cur_time >= start_time:
                    start_time, exec_time = Q.get()
                    answer[score] += cur_time - start_time
                    cur_time      += exec_time
                    break
        else:
            if min_start_time is None:
                break
            else:
                cur_time = min_start_time

    answer[0] = cur_time
    return answer


args = [
    # [[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]]
    [[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]
]
print(solution(*args))
