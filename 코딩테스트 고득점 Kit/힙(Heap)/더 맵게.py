# VERBOSE = False
VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None


from heapq import heapify, heappop, heappush
def solution(scoville, K):
    # nlog(n)
    heapify(scoville)

    answer = 0
    while True:
        if scoville[0] >= K:
            break
        if len(scoville) == 1:
            return -1

        min1 = heappop(scoville)
        min2 = heappop(scoville)
        mix  = min1 + 2*min2
        heappush(scoville, mix)
        answer += 1

    return answer

    # if scoville[0] >= K:
    #     return 0
    #
    # cur_min = 0
    # while cur_min < K:
    #     if len(scoville) == 1:
    #         return -1
    #     min1 = heappop(scoville)
    #     min2 = heappop(scoville)
    #     mix  = min1 + 2*min2
    #     heappush(scoville, mix)
    #     cur_min = scoville[0]
    # return N - len(scoville)

args = [
    [1, 2, 3, 9, 10, 12], 7
]
print(solution(*args))
