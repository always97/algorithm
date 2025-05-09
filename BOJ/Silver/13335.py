n, w, L = map(int, input().split())
truck = list(map(int, input().split()))
bridge = [0] * w

time = 0
bridge_weight = 0

while bridge:
  time += 1
  bridge_weight -= bridge.pop(0)

  if truck:
    ## 다리위에 트럭의 무게가 감당이 되면 추가 아니면 0 추가
    if bridge_weight + truck[0] <= L:
      t = truck.pop(0)
      bridge.append(t)
      bridge_weight += t
    else:
      bridge.append(0)


print(time)