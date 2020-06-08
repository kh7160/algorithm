import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

str = input();
fnl_str = [];

for i in range(len(str)):
    if(str[i] == ' '):
        continue;
    else:
        fnl_str.append(str[i]);

print(''.join(fnl_str));