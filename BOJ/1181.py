n = int(input())
word_set = set([input() for _ in range(n)])
word_lst = [list(_) for _ in word_set]
# print(word_lst)
word_lst.sort(key=lambda x:(len(x), x))
word_lst = [''.join(_) for _ in word_lst]
for _ in word_lst:
    print(_)