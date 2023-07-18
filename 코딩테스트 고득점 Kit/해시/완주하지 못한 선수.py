VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None

from collections import Counter

def solution(participant, completion):
    inp = Counter(participant)
    out = Counter(completion)
    return list(inp - out)[0]

args = [
    ["leo", "kiki", "eden"],
    ["eden", "kiki"]
]
print(solution(*args))
