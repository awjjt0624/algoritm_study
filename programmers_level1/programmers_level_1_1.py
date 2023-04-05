import re


def solution(s):
    answer = True
    start = "("
    end = ")"
    index_start = s.find(start)
    index_end = s.find(end)

    if index_start > index_end or index_start < 0:
        answer = False

    special = re.compile(r'[\)\(]')
    result = special.findall(s)

    check = 0
    for r in result:
        if r == "(":
            check += 1
        elif r == ")":
            check -= 1

        if check < 0:
            answer = False
            break
        else:
            answer = True

    if check > 0:
        answer = False

    return answer


if __name__ == '__main__':
    s = ")()()"
    answer = solution(s)
    print(answer)
