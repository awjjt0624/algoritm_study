# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N, A):
    # Implement your solution here
    counter_array = [0]*N

    max_value = 0
    for number in A:
        if N + 1 == number:
            counter_array = [max_value]*N
        else:
            counter_array[number - 1] += 1
            max_value = max(max_value, counter_array[number - 1])

    return counter_array


if __name__ == '__main__':
    print(solution(5, [3, 4, 4, 6, 1, 4, 4]))