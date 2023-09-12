from collections import deque

def solution(n, t, m, timetable):
    # 처음 기준이 되는 시간은 9:00 셔틀이 9:00부터 출발하기 때문에 540분부터 시작
    shuttle = 540
    timetable = deque(sorted([time_to_minute(time) for time in timetable]))

    # 처음 시간부터 마지막 셔틀 시간까지 반복
    for s in range(shuttle, shuttle+(t*(n)), t):
        cnt = 0
        e = s
        while timetable:
            if timetable[0] <= s and cnt < m:
                cnt += 1
                e = timetable.popleft()
            else:
                break

    if cnt < m:
        return minute_to_time(s)
    else:
        return minute_to_time(e-1)

# 시간을 분으로 변환 타입은 int로
# HH:MM -> minute
def time_to_minute(time):
    h, m = time.split(":")
    minute = int(m) + int(h) * 60
    return minute

def minute_to_time(minute):
    h = minute // 60
    m = minute % 60
    return ':'.join([str(h).zfill(2), str(m).zfill(2)])

n, t, m = 1, 1, 5
timetable = ["08:00", "08:01", "08:02", "08:03"]
print(solution(n,t,m,timetable))