# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # Implement your solution here
    east = 0
    west = 0
    passing = 0

    for a in A:
        if a == 0:
            passing += west
            east += 1
        else:
            passing += east
            west += 1

    return passing


if __name__ == '__main__':
    print(solution([0, 1, 0, 1, 1]))