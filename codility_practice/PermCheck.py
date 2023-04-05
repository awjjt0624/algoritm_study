# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # Implement your solution here
    answer = 1

    A = sorted(A)
    # target_value = sum([i for i in range(1, len(A) + 1)])
    # input_value = sum(A)

    for index, number in enumerate(A, 1):
        if index != number:
            answer = 0
            return answer
    return answer


if __name__ == '__main__':
    # print(solution([1, 4, 1]))
    print(solution([4, 1, 3, 2]))