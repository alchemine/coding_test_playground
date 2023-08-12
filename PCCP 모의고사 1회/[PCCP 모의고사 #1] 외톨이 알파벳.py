# 20m 15s

# VERBOSE = False
VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None

from collections import Counter

def solution(input_string):
    # 1. Count character
    cnt_org   = Counter(input_string)
    cands_cnt = [ch for ch, cnt in cnt_org.items() if cnt >= 2]

    # 2. Filter duplication
    # 2.1 Remove duplicated chars
    s_rm_dup = ""
    ch_last = ''
    for ch in input_string:
        if ch != ch_last:
            s_rm_dup = f"{s_rm_dup}{ch}"
            ch_last = ch
    cnt_rm_dup = Counter(s_rm_dup)
    cands_dup  = [ch for ch, cnt in cnt_rm_dup.items() if cnt > 1]  # select separate chars

    answer = set(cands_cnt) & set(cands_dup)
    answer = ''.join(sorted(answer))
    if len(answer):
        return answer
    else:
        return 'N'


args = [
    # "edeaaabbccd",
    "eeddee"
]
print(solution(*args))
