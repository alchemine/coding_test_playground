# 27m 40s

# VERBOSE = False
VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None

from datetime import datetime

MONTH = 28
YEAR = 12 * 28

def dt2int(dt):
    y, m, d = dt.year, dt.month, dt.day
    return YEAR*y + MONTH*m + d


def timediff(dt1, dt2):
    return dt2int(dt1) - dt2int(dt2)

def solution(today, terms, privacies):
    today = datetime.strptime(today, "%Y.%m.%d")
    terms = {term: int(period)*MONTH for term, period in map(lambda x: x.split(), terms)}

    answer = []
    for id, (date, term) in enumerate(map(lambda x: x.split(), privacies)):
        date   = datetime.strptime(date, "%Y.%m.%d")
        period = terms[term]
        if timediff(today, date) >= period:
            answer.append(1+id)
    return answer

args = [
    "2022.05.19",
    ["A 6", "B 12", "C 3"],
    ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
]
print(solution(*args))
