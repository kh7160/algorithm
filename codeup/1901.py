import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

num = int(input());

def recursion(n):
    if(n == 0):
        return
    print(n)
    recursion(n-1)

recursion(num)