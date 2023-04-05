# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Implement your solution here
    answer = 0
    string_bracket = "(){}[]"
    bracket = {
                        "()": 0, "{\}": 0, "[]": 0
                    }
    close_bracket = [")", "}", "]"]

    test = bracket.keys()
    for s in S:
        if s in bracket.keys() and s in close_bracket:
            bracket[s] -= 1
        else:
            bracket[s] += 1

        if bracket.get(s) < 0:
            answer = 0
            break
    return answer


if __name__ == '__main__':
    input = "([)()]"
    print(solution(input))
