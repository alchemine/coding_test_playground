from collections import defaultdict

# 31m

def solution(id_list, report, k):
    VERBOSE = True
    def log(*msg):
        if VERBOSE: print(*msg)

    # ---

    id_reported = {id: set() for id in id_list}
    for id1, id2 in (ids.split(' ') for ids in report):
        id_reported[id1].add(id2)
    log(id_reported)

    cnt = defaultdict(int)
    for ids in id_reported.values():
        for id in ids:
            cnt[id] += 1

    id_stopped = set()
    for id in cnt:
        if cnt[id] >= k:
            id_stopped.add(id)

    answer = []
    for id, id_rep in id_reported.items():
        answer.append(len(id_rep & id_stopped))
    return answer



# id_list = ["muzi", "frodo", "apeach", "neo"]
# report  = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k = 2

id_list = ["con", "ryan"]
report  = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
print(solution(id_list, report, k))
