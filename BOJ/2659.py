# import sys
# sys.stdin = open("input.txt", "r")

input_num = input().split(' ')
result_set = set()
cnt = 0
def chk_time_num(input_num):
    result_lst = []
    input_num = list(input_num)
    for i in range(4):
        result_lst.append(int(''.join(input_num)))
        input_num = input_num[1:] + list(input_num[0])
    return min(result_lst)

target = chk_time_num(''.join(input_num))

for i in range(1111, target+1):
    if str(i).count('0') == 0:
        # print(i)
        result_set.add(chk_time_num(str(i)))

print(len(result_set))