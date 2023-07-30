VERBOSE = False
# VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None

from collections import defaultdict
from bisect import bisect_left, insort
from itertools import product


def solution(info, query):
    data = defaultdict(list)
    for idx, (lang, position, career, food, score) in enumerate(map(lambda x: x.split(), info)):
        score = int(score)
        for key in list(product([lang, '-'], [position, '-'], [career, '-'], [food, '-'])):
            insort(data[key], score)

    answer = []
    for lang, position, career, food_score in map(lambda x: x.split(' and '), query):
        food, score = food_score.split()
        score = int(score)
        cands = data[lang, position, career, food]
        answer.append(len(cands) - bisect_left(cands, score))
    return answer

args = [
["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]
]
print(solution(*args))
