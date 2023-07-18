# VERBOSE = False
VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None

from collections import defaultdict

def solution(phone_book):
    table = defaultdict(int)
    for num in phone_book:
        for l in range(len(num)):
            table[num[:l+1]] += 1

    for num in phone_book:
        if table[num] > 1:
            return False

    return True


args = [
    ["119", "97674223", "1195524421"]
    # ["12","123","1235","567","88"]
    # ["123","456","789"]
]
print(solution(*args))
