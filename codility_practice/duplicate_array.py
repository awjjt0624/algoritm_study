# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # Implement your solution here
    # sor_a = sorted(A)

    set_a = set(A)

    return len(set_a)


if __name__ == '__main__':
    input = [2,2,2,2,2,2,2,2,2,2]
    # input = [2, 1, 1, 2, 3, 1]
    print(solution(input))
