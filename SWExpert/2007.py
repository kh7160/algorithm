import sys
sys.stdin = open("input.txt", "r")

n = int(input())
for i in range(n):
    text = input()
    if_pattern = False
    for j in range(1,10+1):
        if if_pattern == True:
            break

        pattern = text[:j]
        # print(pattern)
        len_pattern = len(pattern)
        for _ in range(0, len(text), len_pattern):
            if text[_:_+len_pattern] == text[_+len_pattern:_+len_pattern*2]:
                print(f"#{i+1} {len_pattern}")
                if_pattern = True
                break
            else:
                break