def count_binary_one(n):
    binaray_number = bin(n)[2:]
    target_count = 0
    for x in str(binaray_number):
        if int(x) == 1:
            target_count = target_count + 1

    return target_count


def solution(n):
    answer = n
    onecnt = bin(n).count('1')              # N의 2의진수의 1의 갯수
    while True:                             # 무한반복
        answer += 1
        answercnt = bin(answer).count('1')
        if answercnt == onecnt:
            break
    return answer


def solution(n):
    answer = 0

    target_count = count_binary_one(n)

    print(target_count)

    not_complete = True
    while not_complete:
        n += 1
        return_value = count_binary_one(n)

        if target_count == return_value:
            answer = n
            not_complete = False

    return answer


if __name__ == '__main__':
    n = 78
    result = solution(n)
    print(result)
