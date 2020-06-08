sentence = input()
fnl, tmp = 0, 0
for i in range(len(sentence)):
    if sentence[i] == '-':
        if tmp != 0:
            fnl += tmp
            tmp = 0
        for j in range(i+1, len(sentence)):
            if sentence[j].isdigit():
                tmp *= 10
                tmp += int(sentence[j])
            else:
                fnl -= tmp
                tmp = 0
        fnl -= tmp
        tmp = 0
        break
    else:
        if sentence[i].isdigit():
            tmp *= 10
            tmp += int(sentence[i])
        else:
            fnl += tmp
            tmp = 0
fnl += tmp
print(fnl)