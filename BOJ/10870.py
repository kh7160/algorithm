def recur_fibo(n):
    return 0 if n == 0 else\
           1 if n == 1 else\
           recur_fibo(n-1) + recur_fibo(n-2)

n = int(input())
print(recur_fibo(n))