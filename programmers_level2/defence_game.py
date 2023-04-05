def solution(n, k, enemy):
    answer = 0
    temp = []
    min = 1000001

    if k >= len(enemy):
        return len(enemy)

    check_sum = 0
    for round, e in enumerate(enemy, 1):
        if min >= e:
            temp = temp + [e]
            min = e
        else:
            temp = [e] + temp

        if round > k and min >= e:
            check_sum += e
            if check_sum > n:
                return round - 1
            elif check_sum == n:
                return round
            elif check_sum <= n and len(enemy) == round:
                return round
    return answer


if __name__ == '__main__':
    # n, k, enemy = 10, 1, [2, 2, 2, 2, 10]
    # n, k, enemy = 1, 6, [2, 2, 2, 2, 3, 3, 1]
    n, k, enemy = 7, 3, [4, 2, 4, 5, 3, 3, 1]
    # n, k, enemy = 1, 6, [2, 2, 2, 2, 3, 3, 1]

    print(solution(n, k, enemy))
