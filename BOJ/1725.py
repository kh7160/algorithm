import sys
sys.stdin = open("input.txt", "r")

n = int(input())
height = [int(input()) for _ in range(n)]
stack=[]
answer = 0
stack.append((0,height[0]))
for i in range(1,len(height)):
    print(stack)
    if stack[-1][1] < height[i]:
        stack.append((i, height[i]))
    else:
        max_len = i
        while len(stack)!=0 :
            tmp = stack.pop()
            square = tmp[1] * (i-tmp[0])
print(answer)