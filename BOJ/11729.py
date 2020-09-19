def recur_func(n, start, by, end):
    if n == 1:
        stack.append([start, end])
    else:
        recur_func(n-1, start, end, by)
        stack.append([start, end])
        recur_func(n - 1, by, start, end)

n = int(input())
stack = []
recur_func(n, 1, 2, 3)
print(len(stack))
for _ in stack:
    print(*_)