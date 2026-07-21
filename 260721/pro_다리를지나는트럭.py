from collections import deque
def solution(bridge_length, weight, truck_weights):
    waiting = deque(truck_weights)
    bridge = deque([0] * bridge_length)

    current_weight = 0
    time = 0

    while waiting or current_weight > 0:
        time += 1
        out = bridge.popleft()
        current_weight -= out

        if waiting and current_weight + waiting[0] <= weight:
            truck = waiting.popleft()
            bridge.append(truck)
            current_weight += truck
        
        else:
            bridge.append(0)



    return time