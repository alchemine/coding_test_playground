# VERBOSE = False
VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None


from heapq import heappop, heappush
def solution(jobs):
    jobs = sorted(jobs)

    answer   = 0
    t_cur    = 0
    idx_last = 0
    cands    = []
    while True:
        idx = idx_last
        while idx < len(jobs):
            t, l = jobs[idx]
            if t <= t_cur:
                heappush(cands, (l, t))
            else:
                if len(cands) == 0:
                    t_cur = t
                    continue
                else:
                    break
            idx += 1
        idx_last = idx

        l_sel, t_sel = heappop(cands)
        answer += (t_cur - t_sel) + l_sel
        t_cur += l_sel

        if len(cands) == 0 and idx_last == len(jobs):
            break

    return answer // len(jobs)


args = [
    [[0, 3],
     [1, 9],
     [20, 6]]
]
print(solution(*args))
