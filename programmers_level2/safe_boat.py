# def solution(people, limit):
#     answer = 0
#
#     people = sorted(people)
#     while people:
#         a = people.pop(0)
#         index = -1
#         while True:
#             if abs(index) <= len(people):
#                 b = people[index]
#                 if a + b <= limit:
#                     people.pop(index)
#                     answer += 1
#                     break
#                 index -= 1
#             else:
#                 answer += 1
#                 break
#     return answer
#


def solution(people, limit):
    answer = 0

    people = sorted(people)
    start_index = 0
    while start_index <= len(people) - 1:
        if people[start_index] + people[-1] > limit:
            people.pop()
            answer += 1
        else:
            people.pop()
            start_index += 1
            answer += 1
    return answer



if __name__ == '__main__':
    people = [70, 50, 80, 50]
    # people = [70, 80, 50]
    # people = [10, 20, 30, 40]
    limit = 100
    print(solution(people, limit))
