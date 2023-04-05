def solution(s):
    answer = -1
    stack = [x for x in s]
    temp = []

    not_complete = True
    temp_alphabet = ""

    while not_complete:
        if not stack and not temp:
            answer = 1
            break
        elif not stack and temp:
            answer = 0
            break

        stack_alphabet = stack.pop()

        if temp:
            temp_alphabet = temp.pop()

        if temp_alphabet != stack_alphabet and temp_alphabet != '':
            temp.append(temp_alphabet)
            temp.append(stack_alphabet)
        elif temp_alphabet == stack_alphabet:
            temp_alphabet = ''
            continue
        else:
            temp.append(stack_alphabet)

    return answer


# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
# 정답에 가까운 코드 일듯..
def solution(s):
    answer = []
    for i in s:
        if not(answer):
            answer.append(i)
        else:
            if(answer[-1] == i):
                answer.pop()
            else:
                answer.append(i)
    return not(answer)


if __name__ == '__main__':
    s = "baabaa"
    s = "cdcd"
    result = solution(s)
    print(result)
