def find_space(s):
    space_indexes = []

    is_space_continue = False
    space = ""
    for index, s_s in enumerate(s, 1):
        if s_s.isspace():
            is_space_continue = True
            space += " "
        else:
            if is_space_continue:
                space_indexes.append(space)
            is_space_continue = False
            space = ""

        if len(s) == index and is_space_continue:
            space_indexes.append(space)

    return space_indexes


def solution(s):
    answer = ''
    words = s.split()

    space_indexes = find_space(s)
    t = []
    for word in words:
        # x = word[0]
        word = word[0].upper() + word[1:].lower()
        t.append(word)

    for index, t_t in enumerate(t):

        if index + 1 != len(t):
            answer += t_t + space_indexes[index]
        else:
            if len(t) == len(space_indexes):
                answer += t_t + space_indexes[index]
            else:
                answer += t_t

    return answer


def solution_2(s):
    s = s.split(' ')
    total = ""

    for i in s:
        total += i.capitalize()
        total += " "

    total = total.rstrip()
    return total


if __name__ == '__main__':
    s = "for the  last week"
    result = solution_2(s)
    print(s)
    print(result)
