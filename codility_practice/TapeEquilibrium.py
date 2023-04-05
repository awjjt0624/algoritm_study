# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import defaultdict

def solution(A):
    # Implement your solution here
    answer = 0
    # print(sum(A[:1]))
    # print(sum(A[1:]))

    result = defaultdict()
    # [result.setdefault(i, []) for i in range(1, len(A) + 1)]
    for index in range(1, len(A)):
        diff = sum(A[:index]) - sum(A[index:])
        key = abs(diff)
        result.setdefault(key, [])
        # result[index] = diff

    for index in range(1, len(A)):
        diff = sum(A[:index]) - sum(A[index:])
        key = abs(diff)
        result[key].append(index)

    min_value = min([key for key in result.keys()])

    answer = min_value

    return answer


if __name__ == '__main__':

    print(solution([3,1,2,4,3]))

