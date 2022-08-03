# 47m -> 1:23

from collections import defaultdict
from datetime import datetime
import math

def solution(fees, records):
    VERBOSE = True
    def log(*msg):
        if VERBOSE: print(*msg)
    # -----------------------------

    # 1. 각 차량 별 누적 주차 시간 계산
    def get_time_cums(records):
        # 1) 입출차 시간 파악
        stats = defaultdict(list)
        for time, id, stat in map(lambda x: x.split(), records):
            stats[id].append(time)
        for id in list(stats):
            if len(stats[id]) % 2 != 0:
                stats[id].append('23:59')

        # 2) datetime 객체로 만들기
        for id in list(stats):
            stats[id] = list(map(lambda s: datetime.strptime(s, "%H:%M"), stats[id]))

        # 3) 누적 주차 시간 계산
        time_cums = defaultdict(int)
        for id in list(stats):
            for i in range(len(stats[id]) // 2):
                t1 = stats[id][2*i]
                t2 = stats[id][2*i+1]
                cum = (t2 - t1).seconds // 60
                time_cums[id] += cum
        return time_cums

    time_cums = get_time_cums(records)


    # 2. 누적 주차 시간으로부터 주차 요금 계산
    def get_costs_from_time_cums(time_cums, fees):
        base_time, base_fee, unit_time, unit_fee = fees

        # 1) 번호가 작은 순으로 배열
        parking_fees = {id: 0 for id in sorted(time_cums)}

        # 2) 주차 요금 계산
        for id in time_cums:
            time = time_cums[id]
            if time >= base_time:
                parking_fees[id] = base_fee + math.ceil((time - base_time)/unit_time) * unit_fee
            else:
                parking_fees[id] = base_fee
        return parking_fees

    costs = get_costs_from_time_cums(time_cums, fees)
    return list(costs.values())


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))
