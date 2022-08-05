from datetime import datetime
from itertools import cycle
import re


def solution(m, musicinfos):
    VERBOSE = True
    def log(*msg):
        if VERBOSE: print(*msg)
    # -----------------------------

    m = re.sub(r'([A-Z])#', lambda m: m.group(1).lower(), m)
    cands = []
    for start, end, name, music in (musicinfo.split(',') for musicinfo in musicinfos):
        # 1. Process data
        music = re.sub(r'([A-Z])#', lambda m: m.group(1).lower(), music)
        times = (datetime.strptime(end, "%H:%M") - datetime.strptime(start, "%H:%M")).seconds // 60

        # 2. Reconstruct full notes
        music = cycle(music)
        music_full = ''.join(next(music) for i in range(times))
        log(music_full)

        # 3. Search substring
        if re.search(m, music_full) is not None:
            cands.append([times, datetime.strptime(start, "%H:%M").timestamp(), name])

    # 4. Select answer
    if len(cands) == 0:
        return '(None)'

    return max(cands, key=lambda x: (x[0], -x[1]))[2]


m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB",
              "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))
