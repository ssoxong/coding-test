def solution(bridge_length, weight, truck_weights):
    answer=0
    bridge = [0 for i in range(bridge_length)]
    bridge_weight = 0
    
    for index, truck in enumerate(truck_weights):
        while(bridge_weight-bridge[0]+truck>weight):
            bridge_weight-=bridge.pop(0)
            answer+=1
            bridge.append(0)

        bridge_weight-=bridge.pop(0)
        answer+=1
        bridge.append(truck)
        bridge_weight+=truck
        
        if(index==len(truck_weights)-1):
            answer+=bridge_length

    return answer