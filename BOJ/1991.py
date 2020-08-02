# import sys
# sys.stdin = open("input.txt", "r")

def Order(ix):
    if ix == '.':
        return

    result_pre.append(ix)
    Order(tree[ix][0])
    result_in.append(ix)
    Order(tree[ix][1])
    result_post.append(ix)

n = int(input())
tree = {}
for _ in range(n):
    tree_input = input().split()
    tree[tree_input[0]] = tree_input[1:]
# print(tree)

result_pre = []
result_in = []
result_post = []

Order('A')

print(''.join(result_pre), ''.join(result_in), ''.join(result_post), sep='\n')