# 49m 27s

VERBOSE = False
# VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None

from datetime import datetime
from itertools import cycle, islice


NOTE_DIC = {f"{note}#": chr(ord('H') + ord(note)-ord('A')) for note in 'ACDFG'}

def convert(notes):
    for key, value in NOTE_DIC.items():
        notes = notes.replace(key, value)
    return notes

def solution(m, musicinfos):
    # 1. Rearrange music info: str -> int
    m_cvt = convert(m)
    data = {}
    for start_time, end_time, name, notes_unit in map(lambda musicinfo: musicinfo.split(','), musicinfos):
        duration       = (datetime.strptime(end_time, "%H:%M") - datetime.strptime(start_time, "%H:%M")).seconds // 60
        notes_unit_cvt = convert(notes_unit)
        notes          = ''.join(islice(cycle(notes_unit_cvt), duration))
        data[name]     = [duration, start_time, notes]

    # 2. Find all matches
    cands = []
    for name, (duration, start_time, notes) in data.items():
        if m_cvt in notes:
            cands.append([duration, start_time, name])

    if len(cands):
        return min(cands, key=lambda x: (-x[0], x[1]))[2]  # max(duration), min(start_time)
    else:
        return "(None)"


args = [
    # "ABCDEFG",	["12:00,12:14,HELLO,CDEFGAB",
    #              "13:00,13:05,WORLD,ABCDEF"]
    "CC#BCC#BCC#BCC#B",	["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
]
print(solution(*args))
