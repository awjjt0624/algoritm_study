from heapq import heappush, heappop
import operator


def solution(jobs):
    answer = 0

    jobs = sorted(jobs, key=operator.itemgetter(0, 1))


    start, time = jobs.pop(0)

    time_list = []
    wait_list = []
    process_end_time = 0
    heappush(wait_list, (time, start))
    while wait_list:

        time, start = heappop(wait_list)

        if process_end_time < start:
            wait_time = process_end_time - start
            process_end_time = process_end_time + time
            total_time = wait_time + time
        elif process_end_time > start:
            wait_time = process_end_time - start
            process_end_time = process_end_time + time
            total_time = wait_time + time
        else:
            process_end_time = start + time
            total_time = time

        time_list.append(total_time)

        while True:
            if jobs and process_end_time > jobs[0][0]:
                start, time = jobs.pop(0)
                heappush(wait_list, (time, start))
            elif jobs and process_end_time < jobs[0][0]:
                break
            else:
                break

        if jobs and not wait_list:
            start, time = jobs.pop(0)
            heappush(wait_list, (time, start))

    return sum(time_list)//len(time_list)


if __name__ == '__main__':
    # jobs = [[0, 3], [1, 9], [2, 6]]
    jobs = [[0, 3], [1, 9], [2, 6], [19, 2]]
    # jobs = [[0, 100], [5, 10]]
    # jobs = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
    # = 72
    # jobs = [[0, 3]]
    # return 9
    print(solution(jobs))
