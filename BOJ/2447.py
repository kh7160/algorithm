def recur_func(n):
    if n == 3:
        return "***\n* *\n***"
    else:
        pattern = recur_func(n/3)
        print(f"{pattern}")
        return f"{pattern}{pattern}{pattern}\n{pattern} {pattern}\n{pattern}{pattern}{pattern}"

n = int(input())
recur_func(n)