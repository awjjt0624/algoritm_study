def solution(n, lost, reserve):
    answer = 0

    l_index = 0
    r_index = 0
    l_len = len(lost)
    r_len = len(reserve)

    ok_count = 0
    while l_index <= l_len - 1 and r_index <= r_len - 1:
        diff = abs(lost[l_index] - reserve[r_index])
        if 1 >= diff:
            ok_count += 1
            r_index += 1
            l_index += 1
        else:
            l_index += 1

    answer = n - l_len + ok_count
    return answer


if __name__ == '__main__':
    # n = 5
    # lost = [2,4]
    # reserve = [1,3,5]

    # n = 5
    # lost = [5]
    # reserve = [4]

    # n = 5
    # lost = [1,3]
    # reserve = [2,4]

    n, lost, reserve = 7, [2, 4, 7], [1, 3, 5]
    print(solution(n, lost, reserve))
