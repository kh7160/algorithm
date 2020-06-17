x = int(input())
origin = 64
stick_list = [origin]
cnt = 0
while sum(stick_list) != x:
    if sum(stick_list) >= x:
        min = stick_list.pop()
        if min // 2 + sum(stick_list) >= x:
            stick_list.append(min // 2)
        else:
            stick_list.append(min // 2)
            stick_list.append(min // 2)
print(len(stick_list))