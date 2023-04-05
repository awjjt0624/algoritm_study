# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def rotate_B(A, B, rotate=0):
    if rotate == len(A):
        return -1
    for i in range(0, len(B)):
        if A[i] == B[i]:
            rotate_array = [B.pop()]
            rotate_array.extend(B)
            rotate += 1
            return rotate_B(A, rotate_array, rotate)

    return rotate


def solution(A, B):
    # Implement your solution here
    return rotate_B(A, B)


if __name__ == '__main__':
    input = [[1,3,5,2,8,7], [7,1,9,8,5,7]]
    print(solution(input[0], input[1]))
