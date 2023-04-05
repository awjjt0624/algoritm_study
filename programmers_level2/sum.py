def solution(n):
    answer = 0
    for i in range(n):
        val = n
        a = 0
        while val > 0:
            minus_val = (n - a) - i
            if minus_val == 0:
                break
            val = val - minus_val

            if val < 0:
                break
            else:
                if val == 0:
                    answer += 1
                    break
                a += 1

    return answer


if __name__ == '__main__':
    n = 3
    result = solution(n)
    print(result)