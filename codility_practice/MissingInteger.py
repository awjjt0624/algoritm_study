# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    A = sorted(set(A))
    answer = 1
    search_complete = False

    complete = []
    for i in range(len(A)):
        temp_number = A.pop(0)
        if temp_number > 0:
            complete.append(temp_number)

    for j, number in enumerate(complete, 1):
        if j != number:
            answer = j
            search_complete = True
            break

    if not complete:
        answer = 1
    elif not A and complete and not search_complete:
        answer = len(complete) + 1

    return answer

# print(solution([1,3,6,4,1,2]))