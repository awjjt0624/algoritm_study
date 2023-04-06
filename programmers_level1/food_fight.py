def solution(food):
    answer = ''

    for cal, f in enumerate(food):
        answer += (f // 2) * str(cal)

    answer = answer + "0" + answer[::-1]
    return answer


if __name__ == '__main__':
    assert solution([1, 3, 4, 6]) == "1223330333221"
    assert solution([1, 7, 1, 2]) == "111303111"
