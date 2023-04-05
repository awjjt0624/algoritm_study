# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    answer = 1
    if A and len(A) > 0:
        # print(sum(range(1, len(A)+2)))
        answer = sum(range(1, len(A)+2)) - sum(A)
    return answer


if __name__ == '__main__':
    # A = [2,3,1,5]
    # A = [1]
    A = [1]
    print(solution(A))