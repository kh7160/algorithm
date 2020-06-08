def solution(phone_book):
    cnt = 0
    phone_book.sort()
    for _ in phone_book:
        # print(list(map(lambda x: x[:len(_)], phone_book)))
        cnt = list(map(lambda x : x[:len(_)],phone_book)).count(_)
        if cnt != 1:
            return False
        return True


print(solution(['12','123','1235','567','88']))
# print(solution(['119', '97674223', '1195524421']))
# print(solution(['123', '456', '789']))