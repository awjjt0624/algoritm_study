def solution(t, p):
    answer = 0

    for i in range(0, len(t) - len(p) + 1):
        if int(t[i:i + len(p)]) <= int(p):
            answer += 1

    return answer


if __name__ == '__main__':
    assert solution("3141592", "271") == 2
    assert solution("500220839878", "7") == 8
    assert solution("10203", "15") == 3
