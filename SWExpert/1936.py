a, b = map(int, input().split(' '))
result = 'A' if (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2) else\
         'B'

print(result)