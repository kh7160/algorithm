from collections import Counter
n = int(input())
num_lst = [int(input()) for _ in range(n)]
num_lst.sort()
count_lst = Counter(num_lst)
count_lst = count_lst.most_common()
max_cnt = count_lst[0][1]
count_lst = [_ for _ in count_lst if _[1] == max_cnt]
if len(count_lst) > 1:
    count_lst.sort(key=lambda x:x[0])
print(int(round((sum(num_lst)/n), 0)))
print(num_lst[len(num_lst)//2])
print(count_lst[1][0]) if len(count_lst) > 1 else print(count_lst[0][0])
print(num_lst[-1]-num_lst[0])