import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
sys.setrecursionlimit(100000)

num = int(input());

def recursion(n):
    if(n == 1 or n == 2):
        return 1
    return recursion(n-1) + recursion(n-2)

print(recursion(num) % 10009)