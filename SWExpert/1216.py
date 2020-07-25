import sys, math
sys.stdin = open("input.txt", "r")

def round_word(line):
    clss = 0
    for i in range(math.ceil(len(line)/2)):
        if line[i] == line[len(line)-1-i]:
            continue
        else:
            clss = 1
            break

    return len(line) if clss == 0 else 0

for case in range(10):
    n = int(input())
    table = [input() for _ in range(100)]
    pivot = [''.join([table[j][i] for j in range(100)]) for i in range(100)]
    max = 0

    for k in range(100):
        for i in range(100):
            for j in range(i, 100):
                max = round_word(table[k][i:j+1]) if max < round_word(table[k][i:j+1]) else max
                max = round_word(pivot[k][i:j+1]) if max < round_word(pivot[k][i:j+1]) else max

    print(f"#{case+1} {max}")