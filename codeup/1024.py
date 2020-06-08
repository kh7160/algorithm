import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

str = input();

for i in range(len(str)):
    print("'" + str[i] + "'");