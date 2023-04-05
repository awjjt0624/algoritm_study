from itertools import permutations


def solution(A, B):
    answer = 0

    perm = permutations([0, 1, 2, 0, 1, 2], 2)
    a = list(perm)
    print(a)
    for a_a in a:
        print(a_a)
    print(test)

    # selected = defaultdict()
    # for i in range(len(A)):
    #     print(i)
    return answer


if __name__ == '__main__':
    A = [1, 4, 2]
    B = [5, 4, 4]
    answer = solution(A, B)
    print(answer)
