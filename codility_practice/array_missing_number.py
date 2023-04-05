# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    answer = 0
    set_A = set(A)
    sort_set_A = sorted(set_A, key=lambda x: x > 0)
    # print(sort_set_A)

    stack = []
    if sort_set_A[len(set_A) - 1] < 0:
        return 1
    elif sort_set_A[len(set_A) - 1] == len(set_A):
        return len(set_A) + 1

    for i in sort_set_A:
        if not stack:
            stack.append(i)
        else:
            left = stack.pop()
            if left + 1 != i and i > 0:
                return left + 1
            else:
                stack.append(i)


if __name__ == '__main__':
    input = [
        # [1,3,6,4,1,2],
        [1, 2, 3]
        # [-1,-3]
        ]

    for i in input:
        print(solution(i))