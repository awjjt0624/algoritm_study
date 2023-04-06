def solution(a, b, n):
    answer = 0

    while True:
        if n < a:
            break

        answer += (n // a) * b
        n = (n // a) * b + n % a

    return answer


if __name__ == '__main__':
    assert solution(2, 1, 20) == 19
    assert solution(3, 1, 20) == 9
