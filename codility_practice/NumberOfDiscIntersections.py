# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # Implement your solution here
    answer = -1

    temp_arr = []
    for x, radius in enumerate(A):
        lu_set = (x - radius, x + radius)
        # print(lu_set)
        temp_arr.append(lu_set)

    intersec_count = 0
    for index, (start, end) in enumerate(temp_arr):
        for j_index in range(index, len(temp_arr)-1):
            j_start, j_end = temp_arr[j_index + 1]
            if end >= j_start and start <= j_end:
                intersec_count += 1

    if intersec_count > 0:
        answer = intersec_count
    return answer


if __name__ == '__main__':
    input = [1,5,2,1,4,0]
    print(solution(input))