# import sys
# sys.stdin = open("input.txt", "r")

t = int(input())
tot_mm = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for case in range(t):
    f_mm, f_ss, s_mm, s_ss = map(int, input().split(' '))
    if s_mm - f_mm > 0:
        tmp_mm = [f_mm + i + 1 for i in range(s_mm - f_mm - 1)]
        tot_day = sum(tot_mm[i-1] for i in tmp_mm)
        tot_day = tot_day + (tot_mm[f_mm-1] - f_ss + 1) + s_ss
    else:
        tot_day = s_ss - f_ss + 1
    print(f"#{case+1} {tot_day}")