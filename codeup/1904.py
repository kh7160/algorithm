import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

def recursion(a, b):
    if a >= b:
        return
    mid = int(a + (b-a)/2)
    recursion(a, mid)
    if mid % 2 == 1:
        print(mid)
    # recursion(mid, b)
    # if mid % 2 == 1:
    #     print(mid)

recursion(2, 7)