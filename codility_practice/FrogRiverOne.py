# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(X, A):
    # Implement your solution here

    # target_list = [i for i in range(1, X + 1)]

    complete_number = set()
    answer = -1

    for index, number in enumerate(A, 0):
        if number <= X:
            complete_number.add(number)

        if X == len(complete_number):
            answer = index
            return answer

    return answer


if __name__ == '__main__':

    print(solution(7, [1, 3, 1, 4, 2, 3, 5, 4]))
