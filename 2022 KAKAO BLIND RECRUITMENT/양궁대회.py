# 01:26 -> 3:04

from itertools import product

def solution(n, info):
    VERBOSE = True
    def log(*msg):
        if VERBOSE: print(*msg)
    # -----------------------------

    # 1. Action, Reward 계산
    def get_action_reward(info):
        # {action: (reward, cost)}
        rst = {}
        for action in range(11):
            score = 10 - action

            if info[action] > 0:
                reward = score*2
            else:
                reward = score

            if score > 0:
                cost = info[action] + 1
            else:
                cost = 1

            rst[action] = (reward, cost)
        return rst
    action_reward = get_action_reward(info)


    # 2. Consider all situations
    def brute_force(n, action_reward, info):
        # 1) Consider whether to shot the score
        possibilities = list(product(*[[0, 1] for _ in range(11)]))

        # 2) Check validity
        target_reward = sum(10-score for score, shot in enumerate(info) if shot > 0)
        valid_pos = []
        for pos in possibilities:
            sum_cost   = sum(cost*i   for (_, cost), i in zip(action_reward.values(), pos))
            sum_reward = sum(reward*i for (reward, _), i in zip(action_reward.values(), pos))
            if (sum_cost <= n) and (sum_reward > target_reward):
                valid_pos.append((sum_reward, pos))

        if len(valid_pos) == 0:
            return [-1]
        max_reward = max(valid_pos, key=lambda x: x[0])[0]
        valid_pos = [x[1] for x in filter(lambda x: x[0] == max_reward, valid_pos)]

        # 3) Select maximal min shot
        valid_pos = max([pos[::-1] for pos in valid_pos])[::-1]

        # 4) Fill the shots
        rst = []
        sum_costs = 0
        for (_, cost), shot in zip(action_reward.values(), valid_pos):
            if shot:
                sum_costs += cost
                rst.append(cost)
            else:
                rst.append(0)
        shot_remainder = n - sum_costs
        rst[-1] += shot_remainder

        return rst
    return brute_force(n, action_reward, info)


# n = 5
# info = [2,1,1,1,0,0,0,0,0,0,0]

n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]

print(solution(n, info))
