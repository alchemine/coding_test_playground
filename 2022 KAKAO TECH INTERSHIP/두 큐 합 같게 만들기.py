# 27m

# VERBOSE = False
VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None


from collections import deque

def solution(queue1, queue2):
    Q      = queue1 + queue2
    Q1, Q2 = deque(queue1), deque(queue2)

    target, mod = divmod(sum(Q), 2)
    if mod != 0:  # sum of queue should be integer
        return -1

    # sum(Q1) should be target
    answer      = 0
    partial_sum = sum(Q1)
    while True:
        if partial_sum == target:
            break
        elif answer >= 2*len(Q):
            answer = -1
            break
        else:
            answer += 1
            if partial_sum > target:
                elem = Q1.popleft()
                Q2.append(elem)
                partial_sum -= elem
            else:  # partial_sum <= target
                elem = Q2.popleft()
                Q1.append(elem)
                partial_sum += elem

        log(Q1, Q2)

    return answer

args = [
    # [3, 2, 7, 2],	[4, 6, 5, 1]
    # [1, 1], [1, 5]
    [1, 2, 9, 4], [1, 1, 2, 2]
]
print(solution(*args))
