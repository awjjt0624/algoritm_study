# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math


def solution(X, Y, D):
    # Implement your solution here
    answer = 0
    target = Y-X
    if target != 0:
        answer = math.ceil(target / D)
    return answer


if __name__ == '__main__':

    print(solution(40, 80, 30))
