import copy

def solution(info, query):
    answer = []
    info_split = []
    query_split = []
    dict = {}
    for _ in info:
        _ = _.replace('and ', '')
        info_split.append(_.split(' '))
    for _ in query:
        _ = _.replace('and ', '')
        query_split.append(_.split(' '))

    for query in query_split:
        if "'"+str(query)+"'" in list(dict.keys()):
            dict["'"+query+"'"] += 1
            pass

        for info in info_split:
            if (query[0] == '-' or query[0] == info[0]) and\
               (query[1] == '-' or query[1] == info[1]) and\
               (query[2] == '-' or query[2] == info[2]) and\
               (query[3] == '-' or query[3] == info[3]) and\
               (query[0] <= info[0]):
                # print(info)
                dict["'"+str(info)+"'"] = 1
                break
    print(dict)
    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
         ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])