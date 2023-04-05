# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A, K):
    # Implement your solution here
    answer = []
    if A:
        shift_count = K % len(A)

        shift_array = []
        for index in range(shift_count):
            shift_array.append(A.pop())

        shift_array = shift_array[::-1]
        shift_array.extend(A)
        answer = shift_array
    return answer


print(solution([], 3))