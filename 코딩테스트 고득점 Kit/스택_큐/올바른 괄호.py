# VERBOSE = False
VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None

def solution(s):
    stack = []
    for e in s:
        if e == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if len(stack) > 0:
        return False
    else:
        return True

# def solution(s):
#     s = [1 if e == '(' else -1 for e in s]
#     cum_sum = 0
#     for e in s:
#         cum_sum += e
#         if cum_sum < 0:
#             return False
#     if cum_sum > 0:
#         return False
#
#     return True


args = [
    ")()("
]
print(solution(*args))
