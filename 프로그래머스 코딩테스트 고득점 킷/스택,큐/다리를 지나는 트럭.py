from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for _ in range(bridge_length)], maxlen=bridge_length)
    t = 0
    total_truck_weight = 0

    for truck in truck_weights:
        while True:
            t += 1
            total_truck_weight -= bridge[0]
            bridge.popleft()
            if total_truck_weight + truck <= weight:
                total_truck_weight += truck
                bridge.append(truck)
                break
            else:
                bridge.append(0)
    t += len(bridge)
 
    return t

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

print(solution(bridge_length, weight, truck_weights))