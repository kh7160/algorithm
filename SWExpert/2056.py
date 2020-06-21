# import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
for i in range(n):
    temp = input()
    temp_yy, temp_mm, temp_dd = temp[:4], temp[4:6], temp[6:]
    F = lambda x,y: True if (x == '01' or x == '03' or x == '05' or x == '07' or x == '08' or x == '10' or x == '12') and (y >= '01' and y <= '31') else\
                    True if x == '02' and (y >= '01' and y <= '28') else\
                    True if (x == '04' or x == '06' or x == '09' or x == '11') and (y >= '01' and y <= '30') else\
                    False
    if F(temp_mm, temp_dd) == True:
        print(f"#{i+1} {temp_yy}/{temp_mm}/{temp_dd}")
    else:
        print(f'#{i+1} -1')