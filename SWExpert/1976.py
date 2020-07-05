# import sys
# sys.stdin = open("input.txt", "r")

t = int(input())
for case in range(t):
    hh, mm, ex_hh, ex_mm = map(int, input().split(' '))
    if mm + ex_mm < 60:
        hh, mm = hh + ex_hh, mm + ex_mm
    else:
        hh, mm = hh + ex_hh + 1, mm + ex_mm - 60
    hh = hh % 12 if hh % 12 != 0 else\
         12
    print(f"#{case+1} {hh} {mm}")