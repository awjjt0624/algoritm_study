def solution(n):
    answer = 0

    n_1 = 0
    n_2 = 1

    for i in range(n-1):
        current = n_1
        n_1 = n_2
        n_2 = n_1 + current

    answer = n_2 % 1234567
    return answer


if __name__ == '__main__':
    n = 100000
    result = solution(n)
    print(result)
