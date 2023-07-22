# VERBOSE = False
VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None

def solution(arr):
    answer = []
    last_num = None
    for num in arr:
        if num == last_num:
            continue
        last_num = num
        answer.append(last_num)
    return answer

args = [
    [1,1,3,3,0,1,1]
]
print(solution(*args))
