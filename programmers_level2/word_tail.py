def solution(n, words):
    answer = []

    complete = []
    for index, word in enumerate(words):

        if word in complete:
            answer = [(index % n) + 1, (index // n) + 1]
            break

        if not complete:
            complete.append(word)
        elif complete[-1][len(complete[-1])-1:] == word[:1]:
            complete.append(word)
        else:
            answer = [(index % n) + 1, (index // n) + 1]
            break

    if len(words) == len(complete):
        answer = [0, 0]
    return answer


# def solution(n, words):
#     for i in range(1, len(words)):
#         if words[i][0] != words[i-1][-1]  or words[i] in words[:i] :
#             return [(i % n)+1, (i // n)+1]
#     else:
#         return [0,0]


if __name__ == '__main__':
    # words = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"] #[0, 0]

    # words = ["hello", "one", "even", "never", "now", "world", "draw"] # [1, 3]

    words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]  # [3, 3]
    n = 3

    # words = ['qwe', 'eqwe', 'eqwe']
    # n = 2
    result = solution(n, words)
    print(result)
