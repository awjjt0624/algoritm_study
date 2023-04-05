import heapq
import operator


def solution(jobs):
    answer = 0

    processing_end = 0
    wait_time_list = []
    pending_list = []
    go_on = True
    end_time = 0
    jobs = sorted(jobs, key=operator.itemgetter(0, 1))

    while True:
        if jobs:
            start, end = jobs.pop(0)
        else:
            go_on = False
        if processing_end == 0:
            processing_end = end + start
            end_time = end + start
            wait_time_list.append(end)
        else:
            if start < processing_end and go_on:
                # pending_list.append([start, end])
                heapq.heappush(pending_list, (end, [start, end]))
            elif not go_on:
                if pending_list:
                    for p_time, p in pending_list:
                        time = p_time + (end_time - p[0])
                        wait_time_list.append(time)
                        end_time = end_time + p_time

                    pending_list = []
                else:
                    return sum(wait_time_list)//len(wait_time_list)
            else:
                if pending_list:
                    for p_time, p in pending_list:
                        time = p_time + (end_time - p[0])
                        wait_time_list.append(time)
                        end_time = end_time + p_time

                    pending_list = []
                heapq.heappush(pending_list, (end, [start, end]))


if __name__ == '__main__':
    # jobs = [[0, 3], [1, 9], [2, 6]]
    # jobs = [[0, 3], [1, 9], [2, 6], [19, 2]]
    # jobs = [[0, 100], [5, 10]]
    jobs = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
    # = 72
    # jobs = [[0, 3]]
    # return 9
    print(solution(jobs))
