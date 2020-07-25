import sys
sys.stdin = open("input.txt", "r")

ecry_num = [ '0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011' ]
t = int(input())
for case in range(t):
    n, m = map(int, input().split())
    table = [input() for _ in range(n)]
    for i in range(m-7):
        for j in range(n):
            rslt_lst = []
            if table[j][i:i+7] in ecry_num:
                # print(j,i, table[j][i:i+7])
                try:
                    rslt_lst.append(ecry_num.index(table[j][i:i+7]))
                    rslt_lst.append(ecry_num.index(table[j][i+7:i + 14]))
                    rslt_lst.append(ecry_num.index(table[j][i+14:i + 21]))
                    rslt_lst.append(ecry_num.index(table[j][i+21:i + 28]))
                    rslt_lst.append(ecry_num.index(table[j][i+28:i + 35]))
                    rslt_lst.append(ecry_num.index(table[j][i+35:i + 42]))
                    rslt_lst.append(ecry_num.index(table[j][i+42:i + 49]))
                    rslt_lst.append(ecry_num.index(table[j][i+49:i + 56]))
                except:
                    continue
                break
        if len(rslt_lst) != 0:
            break
    rslt = sum(rslt_lst) if (sum(rslt_lst[::2])*3 + sum(rslt_lst[1::2])) % 10 == 0 else 0
    print(f"#{case+1} {rslt}")