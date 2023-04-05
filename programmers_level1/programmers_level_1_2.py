from itertools import *


def solution(numbers, target):
    answer = 0
    length = len(numbers)
    plus_minus = [1, -1]
    result = list(product(plus_minus, repeat=length))

    result_array = []
    for r in result:
        sum_r = 0
        cross = [r[index] * n for index, n in enumerate(numbers, 0)]
        for c in cross:
            sum_r += c

        result_array.append(sum_r)

    print(result_array)
    for ra in result_array:
        if ra == target:
            answer += 1

    return answer


if __name__ == '__main__':
    s = [1, 1, 1, 1, 1]
    answer = solution(s, 3)
    print(answer)
