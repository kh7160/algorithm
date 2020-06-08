import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

hour, min = map(int, input().split());

before30 = min - 30;
if(before30 < 0):
    if(hour == 0):
        hour = 23;
    else:
        hour = hour - 1;
    min = 60 + before30;
else:
    min = before30;

print(hour, min);