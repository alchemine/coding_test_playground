VERBOSE = False
# VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None

import re
from dataclasses import dataclass
from collections import defaultdict


n_cols = n_rows = 51

@dataclass
class Cell:
    v : 'value' = None

    def empty(self):
        return self.v is None

def solution(commands):
    maps   = defaultdict(Cell)
    answer = []

    for command in commands:
        log(command)
        if parsed := re.search("UPDATE ([\d]+) ([\d]+) ([a-z0-9]+)", command):
            r, c, v = parsed.groups()
            cell = maps[r, c]
            for r, c in [(r, c) for r, c in maps if maps[r, c] is cell]:
                maps[r, c].v = v
        elif parsed := re.search("UPDATE ([^\s]+) ([a-z0-9]+)", command):
            v1, v2 = parsed.groups()
            for r, c in [(r, c) for r, c in maps if maps[r, c].v == v1]:
                maps[r, c].v = v2
        elif parsed := re.search("MERGE ([\d]+) ([\d]+) ([\d]+) ([\d]+)", command):
            r1, c1, r2, c2 = parsed.groups()
            cell1 = maps[r1, c1]
            cell2 = maps[r2, c2]

            if (cell1.empty()) and (cell2.empty()):
                for r, c in [(r, c) for r, c in maps if maps[r, c] is cell2]:
                    maps[r, c] = cell1
            elif (cell1.empty()) and (not cell2.empty()):
                for r, c in [(r, c) for r, c in maps if maps[r, c] is cell1]:
                    maps[r, c] = cell2
            elif (not cell1.empty()) and (cell2.empty()):
                for r, c in [(r, c) for r, c in maps if maps[r, c] is cell2]:
                    maps[r, c] = cell1
            elif (not cell1.empty()) and (not cell2.empty()):
                for r, c in [(r, c) for r, c in maps if maps[r, c] is cell2]:
                    maps[r, c] = cell1
        elif parsed := re.search("UNMERGE ([\d]+) ([\d]+)", command):
            r, c = parsed.groups()
            cell = maps[r, c]
            for r, c in [k for k in maps if maps[k] is cell and k != (r, c)]:
                maps[r, c] = Cell()
        elif parsed := re.search("PRINT ([\d]+) ([\d]+)", command):
            r, c = parsed.groups()
            if maps[r, c].empty():
                answer.append("EMPTY")
            else:
                answer.append(maps[r, c].v)
        else:
            raise ValueError

        log(maps)

    return answer

args = [
    # ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
    ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]
]
print(solution(*args))
