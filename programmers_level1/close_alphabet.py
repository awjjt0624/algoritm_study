def solution(s):
    answer = []

    is_exist = {}
    for index, alpha in enumerate(s):
        if alpha not in is_exist:
            answer.append(-1)
        else:
            answer.append(index - is_exist[alpha])
        is_exist[alpha] = index
    return answer


if __name__ == '__main__':
    assert solution("banana") == [-1, -1, -1, 2, 2, 2]
    assert solution("foobar") == [-1, -1, 1, -1, -1, -1]
