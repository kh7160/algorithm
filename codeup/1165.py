import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

time, score = map(int, input().split());

score = score + 1 + (89 - time) / 5;
print(int(score));