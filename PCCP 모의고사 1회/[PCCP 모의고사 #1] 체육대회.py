# 21m -> 29m

# VERBOSE = False
VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None

from itertools import combinations, permutations

def solution(ability):
    n_students, n_sports = len(ability), len(ability[0])
    answer = 0

    for comb_base in combinations(range(n_students), n_sports):
        for comb in permutations(comb_base):
            score = sum(ability[comb[idx_sport]][idx_sport] for idx_sport in range(n_sports))
            answer = max(answer, score)
    return answer

args = [
    [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]
]
print(solution(*args))
