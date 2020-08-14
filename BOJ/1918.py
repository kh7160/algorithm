import sys
sys.stdin = open("input.txt", "r")
priority = {
    '*' : 2,
    '/' : 2,
    '+' : 1,
    '-' : 1
}
stack = []
for _next in '(' + input() + ')':
    if 'A' <= _next <= 'Z':
        print(_next, end='')
    elif _next == '(':
        stack.append(_next)
    elif _next == ')':
        while True:
            temp = stack.pop()
            if temp == '(':
                break
            print(temp, end='')
    else:
        print(stack)
        while stack[-1] != '(' and priority[_next] <= priority[stack[-1]]:
            print(stack.pop(), end='')
        stack.append(_next)