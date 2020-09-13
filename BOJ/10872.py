def recur_func(n):
    if n == 1 or n == 0:
        return 1

    return n * recur_func(n-1)

n = int(input())
result = recur_func(n)
print(result)