def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_weight = [0] * bridge_length
    truck_weights = truck_weights[::-1]
    while len(truck_weights) > 0:
        answer += 1
        bridge_weight.pop(0)
        if sum(bridge_weight) + truck_weights[-1] <= weight:
            bridge_weight.append(truck_weights.pop())
        else:
            bridge_weight.append(0)
    return answer + bridge_length

print(solution(100, 100, [10]*10))