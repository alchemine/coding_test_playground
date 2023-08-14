VERBOSE = False
# VERBOSE = True
log = lambda *msg: print(*msg) if VERBOSE else None


from datetime import datetime, timedelta
from collections import deque, OrderedDict

DATE_FORMAT = "%H:%M"
str2time    = lambda s: datetime.strptime(s, DATE_FORMAT)
time2str    = lambda t: t.strftime(DATE_FORMAT)
START_TIME  = str2time("09:00")

def solution(n,	t,	m,	timetable):
    # 1. Get bus times
    bus_info = OrderedDict({START_TIME + i*timedelta(minutes=t): deque() for i in range(n)})

    # 2. Count crews
    Q = deque(map(str2time, sorted(timetable)))
    for t_bus in bus_info:
        log("[Start]", t_bus, bus_info)
        while Q and (Q[0] <= t_bus) and (len(bus_info[t_bus]) < m):
            t_crew = Q.popleft()
            bus_info[t_bus].append(t_crew)
        log("[End]", t_bus, bus_info)

    # 3. Case study
    if sum(map(len, bus_info.values())) == n*m:  # 모두 탑승한 경우
        last_t_crew_in_last_bus = bus_info[max(bus_info)].pop()    # 마지막 버스를 탈 수 있도록
        t_answer = last_t_crew_in_last_bus - timedelta(minutes=1)  # 마지막 탑승자보다 1분 일찍 오기
    else:
        if len(bus_info) == 1:  # 버스가 1개
            t_answer = list(bus_info)[0]  # 유일한 버스 아슬아슬하게 탑승
        else:  # 버스가 여러 개
            t_last_bus = max(bus_info)  # 마지막 버스를 타야됨
            if len(bus_info[t_last_bus]) < m:  # 마지막 버스 자리가 남아 있으면,
                t_answer = t_last_bus  # 아슬아슬하게 탑승
            else:  # 자리가 없으면,
                last_t_crew_in_last_bus = bus_info[t_last_bus].pop()       # 마지막 버스를 탈 수 있도록
                t_answer = last_t_crew_in_last_bus - timedelta(minutes=1)  # 마지막 탑승자보다 1분 일찍 오기

    return time2str(t_answer)


args = [
    # 2, 10, 2, ["09:10", "09:09", "08:00"]
    # 2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]
    # 1,	1,	1,	["23:59"]
    # 10,	60,	45,	["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
    # 10, 60, 10, ["17:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
]
print(solution(*args))
