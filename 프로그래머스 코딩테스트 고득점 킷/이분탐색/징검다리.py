def solution(distance, rocks, n):
    answer = 0
    
    # 바위정렬
    rocks.sort()
    
    # left, right
    left = 0
    right = distance

    while left <= right:
        # mid, 전 바위위치, 지워진 바위 수, 바위사이 최소값
        mid = (left + right) // 2
        rock_point = 0
        rock_rm = 0
        rock_min = 1e9

        for rock in rocks:
            if rock - rock_point < mid:
                rock_rm += 1
            else:
                rock_min = min(rock_min, rock - rock_point)
                rock_point = rock
        if distance - rock_point < mid:
            rock_rm += 1
        else:
            rock_min = min(rock_min, distance - rock_point)

        if rock_rm <= n:
            left = mid + 1
            answer = rock_min
        else:
            right = mid - 1

    return answer


# distance, rocks, n = 25, [2,14,11,21,17], 2
# distance, rocks, n = 4, [1,2,3], 2
distance, rocks, n = 23, [3,6,9,10,14,17], 2
# distance, rocks, n = 34, [5,19,28], 2
print(solution(distance, rocks, n))