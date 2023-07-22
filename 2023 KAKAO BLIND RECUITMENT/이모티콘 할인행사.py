# 2h 17m 30s

VERBOSE = False
# VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None


from itertools import product

def solution(users, emoticons):
    n_users_plus = {}
    costs        = {}

    dis_rates_comb = [[10, 20, 30, 40] for _ in range(len(emoticons))]
    dis_rates_comb = product(*dis_rates_comb)

    for dis_rates in dis_rates_comb:
        n_user_plus = cost = 0
        for base_rate, base_price in users:
            dis_price = sum((1-dis_rate/100)*emot_price for dis_rate, emot_price in zip(dis_rates, emoticons) if dis_rate >= base_rate)
            if dis_price >= base_price:
                n_user_plus += 1
                continue
            else:
                cost += dis_price
        n_users_plus[dis_rates] = n_user_plus
        costs[dis_rates]        = cost

    n_user_plus = max(n_users_plus.values())
    cost        = max(int(v) for k, v in costs.items() if n_users_plus[k] == n_user_plus)

    log("n_users_plus:", n_users_plus)
    log("costs:", costs)

    return [n_user_plus, cost]

args = [
    [[40, 10000], [25, 10000]],
    [7000, 9000]
]
print(solution(*args))
