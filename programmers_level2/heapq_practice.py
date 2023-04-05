import heapq


def solution(scoville, K):
    answer = 0
    min = 0

    heapq.heapify(scoville)

    while True:

        parent_zero = scoville[0]
        if len(scoville) == 1:
            if parent_zero > K:
                return answer
            else:
                return -1
        if parent_zero < K:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            result = first + second * 2
            heapq.heappush(scoville, result)
            answer += 1
        else:
            break

    return answer


if __name__ == '__main__':
    # scoville = [1, 2, 3, 9, 10, 12]
    scoville = [1,1,1]
    # scoville = [4, 2, 3, 9, 10, 12]
    # K = 7
    K = 2
    # return 2
    print(solution(scoville, K))
