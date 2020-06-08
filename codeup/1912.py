import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
sys.setrecursionlimit(100000)

num = int(input());

def recursion(n):
    if(n == 1):
        return 1
    return n * recursion(n-1)

print(recursion(num))