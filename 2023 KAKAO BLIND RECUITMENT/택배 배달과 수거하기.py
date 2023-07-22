# 1h 12m 30s

VERBOSE = False
# VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None

def solution(cap, n, deliveries, pickups):
    arr1 = deliveries
    arr2 = pickups

    dists1 = []
    while arr1:
        max_dist1 = 0
        cap1 = 0
        while (cap1 < cap) and arr1:
            dcap1 = cap - cap1
            if arr1[-1] == 0:
                arr1.pop()
            elif dcap1 >= arr1[-1]:
                max_dist1 = max(max_dist1, len(arr1))
                cap1 += arr1.pop()
            elif dcap1 == 0:
                continue
            else:
                max_dist1  = max(max_dist1, len(arr1))
                arr1[-1] -= dcap1
                cap1     += dcap1
        dists1.append(max_dist1)
        log(arr1, max_dist1)

    dists2 = []
    while arr2:
        max_dist2 = 0
        cap2 = 0
        while (cap2 < cap) and arr2:
            dcap2 = cap - cap2
            if arr2[-1] == 0:
                arr2.pop()
            elif dcap2 >= arr2[-1]:
                max_dist2 = max(max_dist2, len(arr2))
                cap2 += arr2.pop()
            elif dcap2 == 0:
                break
            else:
                max_dist2  = max(max_dist2, len(arr2))
                arr2[-1] -= dcap2
                cap2     += dcap2
        dists2.append(max_dist2)
        log(arr2, max_dist2)

    answer = 0
    for i in range(max(len(dists1), len(dists2))):
        d1 = dists1[i] if i < len(dists1) else 0
        d2 = dists2[i] if i < len(dists2) else 0
        answer += max(d1, d2)
    return 2*answer

args = [
    1,
    2,
    [0, 0],
    [0, 0],
]
print(solution(*args))
